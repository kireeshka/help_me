import time
import speech
import pygame
import set
import pygame.freetype as pf


class NPC():
    def __init__(self, pos, imag):
        self.speedx = 1
        self.speedy = 0
        self.t = 1
        self.speach = speech.Speech('Привет. меня зовут Машаайуаfefefef', [set.wi // 2, set.hi - 100])
        self.pos = pos
        self.imag = pygame.transform.scale(imag, [set.sizenew * 1.5, set.sizenew * 1.5])
        self.rect = pygame.Rect(self.pos, [set.sizenew * 1.5, set.sizenew * 1.5])


    def draw(self, dp, cam1):
        newr = cam1.newrect(self.rect)
        dp.blit(self.imag, newr)
        if self.t == 0:
            self.speach.draw(dp)


    def update(self):
        if self.t == 1:
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.x > self.pos[0] + 200:
                self.rect.x -= 3
                self.speedx = 0
                self.speedy = -2
            elif self.rect.y > self.pos[1] + 200:
                self.rect.y -= 3
                self.speedx = 2
                self.speedy = 0

            elif self.rect.y < self.pos[1] - 200:
                self.rect.y += 3
                self.speedx = -2
                self.speedy = 0
            elif self.rect.x < self.pos[0] - 200:
                self.rect.x += 3
                self.speedx = 0
                self.speedy = 2




