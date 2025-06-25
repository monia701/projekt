import pygame
import random
from settings import *
from player import Player

# --- Inicjalizacja pygame ---
pygame.init()
pygame.mixer.init()

# --- MUZYKA ---
pygame.mixer.music.load("assets/sounds/MyVeryOwnDeadShip.ogg")
pygame.mixer.music.play(-1)  # -1 = zapętlanie

# --- EKRAN ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra kosmos")
clock = pygame.time.Clock()

# --- TŁO ---
bg = pygame.image.load("assets/images/arena.png").convert()
bg_width = bg.get_width()
scroll_x = 0

# --- CZCIONKA ---
font = pygame.font.SysFont("arial", 36)

# --- Funkcje menu ---
def show_start_menu():
    screen.fill((0, 0, 0))

    title1 = font.render("Gra na zaliczenie przedmiotu:", True, YELLOW)
    title2 = font.render("Ferenc Wiktoria", True, PINK)
    title3 = font.render("Grzesło Monika", True, PINK)
    start_msg = font.render("Naciśnij ENTER, aby zacząć", True, WHITE)

    screen.blit(title1, ((WIDTH - title1.get_width()) // 2, HEIGHT // 2 - 100))
    screen.blit(title2, ((WIDTH - title2.get_width()) // 2, HEIGHT // 2 - 50))
    screen.blit(title3, ((WIDTH - title3.get_width()) // 2, HEIGHT // 2))
    screen.blit(start_msg, ((WIDTH - start_msg.get_width()) // 2, HEIGHT // 2 + 100))

    pygame.display.flip()

    # --- Pętla czekania ---
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def show_end_menu(winner):
    screen.fill((0, 0, 0))
    end_text = font.render(f"{winner} wygrał!", True, YELLOW)
    play_again_msg = font.render("ENTER - Zagraj jeszcze raz", True, WHITE)
    exit_msg = font.render("ESC - Wyjdź", True, WHITE)

    screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2 - 80))
    screen.blit(play_again_msg, (WIDTH // 2 - 220, HEIGHT // 2))
    screen.blit(exit_msg, (WIDTH // 2 - 120, HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    play_again = False
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play_again = True
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
    return play_again

# --- Funkcja zapisu wyniku ---
def save_result(winner):
    with open("wyniki.txt", "a") as file:
        file.write(f"{winner} wygrał\n")

# --- Funkcja rysowania HP ---
def draw_health():
    p1_text = font.render(f"P1 HP: {player1.hp}", True, WHITE)
    p2_text = font.render(f"P2 HP: {player2.hp}", True, WHITE)
    screen.blit(p1_text, (20, 20))
    screen.blit(p2_text, (WIDTH - 200, 20))

# --- Klasa Heart (power-up) ---
class Heart:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.image = pygame.image.load("assets/images/heart.png")
        self.image = pygame.transform.scale(self.image, (40, 40))

    def draw(self, screen, scroll_x):
        screen.blit(self.image, (self.rect.x - scroll_x, self.rect.y))

# --- Pętla gry z możliwością restartu ---
game_running = True
while game_running:
    show_start_menu()

    # --- RESET graczy ---
    player1 = Player(400, HEIGHT - PLAYER_HEIGHT - 50, "Gracz1", pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_f)
    player2 = Player(1200, HEIGHT - PLAYER_HEIGHT - 50, "Gracz2", pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_RETURN)

    # --- Power-up ---
    heart_timer = 300  # co ile klatek pojawia się serduszko (~5 sekund)
    heart = None

    running = True
    while running:
        clock.tick(FPS)

        # --- Kamera ---
        center_between_players = (player1.rect.centerx + player2.rect.centerx) // 2
        scroll_x = center_between_players - WIDTH // 2
        scroll_x = max(0, min(scroll_x, bg_width - WIDTH))

        screen.blit(bg, (-scroll_x, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False

        keys = pygame.key.get_pressed()
        player1.handle_input(keys)
        player2.handle_input(keys)

        player1.update()
        player2.update()

        # --- Kolizja i obrażenia ---
        if player1.attacking and player1.rect.colliderect(player2.rect):
            player2.take_damage()
            player1.attacking = False
        if player2.attacking and player2.rect.colliderect(player1.rect):
            player1.take_damage()
            player2.attacking = False

        # --- Rysowanie graczy ---
        player1.draw(screen, player1.rect.x - scroll_x)
        player2.draw(screen, player2.rect.x - scroll_x)
        draw_health()

        # --- Power-up (Heart) ---
        if heart is None:
            heart_timer -= 1
            if heart_timer <= 0:
                # Losowe miejsce
                heart_x = random.randint(100, bg_width - 100)
                heart_y = HEIGHT - 50 - 40  # na ziemi
                heart = Heart(heart_x, heart_y)
                heart_timer = 300  # reset

        # Rysowanie serduszka
        if heart is not None:
            heart.draw(screen, scroll_x)

            # Sprawdzanie kolizji z graczami
            if player1.rect.colliderect(heart.rect):
                player1.hp = min(player1.hp + 1, 10)
                heart = None
            elif player2.rect.colliderect(heart.rect):
                player2.hp = min(player2.hp + 1, 10)
                heart = None

        # --- Warunek końca gry ---
        if player1.hp <= 0 or player2.hp <= 0:
            winner = "Gracz 1" if player1.hp > 0 else "Gracz 2"
            save_result(winner)
            play_again = show_end_menu(winner)
            if play_again:
                running = False  # wraca do show_start_menu
            else:
                running = False
                game_running = False

        pygame.display.flip()

# --- Koniec gry ---
pygame.quit()
