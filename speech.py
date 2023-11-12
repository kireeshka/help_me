import pygame.freetype as pf
import pygame

import set


class Speech:
    def __init__(self, txt, pos):
        self.txt = txt
        self.pos = pos
        self.wri = pf.Font('lato-light.ttf', 40)
        self.b = 0
        self.phon = pygame.image.load('phon.jpg')
        self.phon = pygame.transform.scale(self.phon,[set.wi,150])

    def draw(self, dp):
        dp.blit(self.phon, [0, set.hi - 150])
        self.wri.render_to(dp, self.pos, self.txt[0:int(self.b) + 1])
        if self.b < len(self.txt) - 1:
            self.b += 0.5

