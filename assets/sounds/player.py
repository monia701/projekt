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
        pass

    def update(self):
        pass

    def take_damage(self):
        pass

    def draw(self, screen, screen_x):
        pass
