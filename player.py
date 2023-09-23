import pygame as p
from helper import Sprite_sheet
from pygame.math import Vector2
"""класс для персонажа"""
class Player(p.sprite.Sprite):
    speed = 5
    def __init__(self,sprite_sheet_paf,position):
        """инит ключевых переменных"""
        super().__init__()
        self.sprite_sheet = Sprite_sheet(sprite_sheet_paf)
        self.image = self.sprite_sheet.get_image(0,0,32,32)
        self.rect = self.image.get_rect(center = position)
    def _move(self):
        """движение персонажа по x,y"""
        self.velocity = Vector2(0,0)
        keys = p.key.get_pressed()
        if keys[p.K_w]: #нажатие на клавишу w
            self.velocity.y = -1
        if keys[p.K_s]: #нажатие на клавишу s
            self.velocity.y = 1
        if keys[p.K_a]: #нажатие на клавишу a
            self.velocity.x = -1
        if keys[p.K_d]: #нажатие на клавишу d
            self.velocity.x = 1
        # делаем чтобы можно было двигаться в одном направлении
        if self.velocity.length() > 1:
            self.velocity.x = 0
        self.velocity *= Player.speed
        self.rect.center += self.velocity
    def update(self):
        """обновление местоположения персонажа """
        self._move()