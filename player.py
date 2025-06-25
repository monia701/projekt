import pygame
from settings import *
from game_object import GameObject

class Player(GameObject):
    def __init__(self, x, y, name, left, right, jump_key, attack):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.name = name
        self.left = left
        self.right = right
        self.jump_key = jump_key
        self.attack = attack
        self.vel_y = 0
        self.on_ground = False
        self.hp = 10
        self.attacking = False
        self.state = "stand"
        self.attack_cooldown = 0
        self.hurt_timer = 0
        self.hit_sound = pygame.mixer.Sound("assets/sounds/hit.wav")

    def handle_input(self, keys):
        if self.hurt_timer > 0:
            return
        self.state = "stand"
        if keys[self.left]:
            self.rect.x -= PLAYER_SPEED
            self.state = "walk"
        if keys[self.right]:
            self.rect.x += PLAYER_SPEED
            self.state = "walk"
        if keys[self.jump_key] and self.on_ground:
            self.vel_y = JUMP_FORCE
            self.on_ground = False
            self.state = "jump"
        if keys[self.attack] and self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 30
            self.state = "attack"

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack_cooldown == 0:
            self.attacking = False

        if self.hurt_timer > 0:
            self.hurt_timer -= 1
            self.state = "hurt"

    def take_damage(self):
        self.hp -= 1
        self.hurt_timer = 15
        self.state = "hurt"
        self.hit_sound.play()

    def draw(self, screen, screen_x):
        image_path = f"assets/images/{self.name.lower()}_{self.state}.png"
        try:
            image = pygame.image.load(image_path)
        except:
            image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
            image.fill((255, 0, 255))
        image = pygame.transform.scale(image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Miganie przy obrażeniu
        if self.hurt_timer > 0 and (self.hurt_timer // 5) % 2 == 0:
            image.set_alpha(128)
        else:
            image.set_alpha(255)

        screen.blit(image, (screen_x, self.rect.y))

        # Pasek życia
        bar_width = PLAYER_WIDTH
        bar_height = 10
        fill = int(bar_width * (self.hp / 10))
        bar_x = screen_x
        bar_y = self.rect.y - 15
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, fill, bar_height))
