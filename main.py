# --- Inicjalizacja pygame ---
pygame.init()
pygame.mixer.init()

# --- EKRAN ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra kosmos")
clock = pygame.time.Clock()

# --- MUZYKA ---
pygame.mixer.music.load("assets/sounds/MyVeryOwnDeadShip.ogg")
pygame.mixer.music.play(-1)  # -1 = zapętlanie


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

