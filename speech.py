import pygame.freetype as pf
import pygame

import set


class Speech:
    def __init__(self, txt, pos):
        self.txt = txt
        self.txtx = []
        if len(self.txt) > 30:
            self.txtx.append(self.txt[0:len(self.txt) // 2])
            self.txtx.append(self.txt[len(self.txt) // 2:])
        else:
            self.txtx.append(self.txt)
        self.num = 0

        self.pos = pos
        self.wri = pf.Font('lato-light.ttf', 40)
        self.b = 0
        self.phon = pygame.image.load('phon.jpg')
        self.phon = pygame.transform.scale(self.phon, [set.wi, 150])

    def draw(self, dp):
        stro = self.txtx[self.num]
        dp.blit(self.phon, [0, set.hi - 150])
        self.wri.render_to(dp, self.pos, stro[0:int(self.b) + 1])
        if self.b < len(self.txtx[self.num]) - 1:
            self.b += 0.5

        if self.num < len(self.txtx) - 1 and len(stro) - 1 <= self.b:
            self.num += 1
            self.b = 0
