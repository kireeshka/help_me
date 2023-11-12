import pygame
import set

class Cam():
    def __init__(self):
        self.x = 0
        self.y = 0
    def shpion(self,pl,map):
        self.x = pl.rect.x * -1 + set.wi // 2
        self.y = pl.rect.y * -1 + set.hi // 2
        if pl.rect.x < set.wi / 2 :
            self.x = 0
        if pl.rect.y < set.hi / 2:
            self.y = 0
        if pl.rect.x + set.wi // 2 >= map.width:
            self.x = -(map.width - set.wi)
        if pl.rect.y + set.hi // 2 >= map.strr:
            self.y = -(map.strr - set.hi)

    def newrect(self,oldrect):
        rect = pygame.Rect(oldrect.x + self.x, oldrect.y + self.y,oldrect.w,oldrect.h)
        return rect
