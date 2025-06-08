# --- Inicjalizacja pygame ---
pygame.init()
pygame.mixer.init()

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