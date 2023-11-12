import pygame as p
from helper import Sprite_sheet
from pygame.math import Vector2
import set
import speech
"""класс для персонажа"""


class Player(p.sprite.Sprite):
    speed = 5

    def __init__(self, sprite_sheet_paf, position):
        """инит ключевых переменных"""
        super().__init__()
        sprite_sheet = Sprite_sheet(sprite_sheet_paf, 2)
        self.velocity = Vector2(0, 0)
        self._loadiamg(sprite_sheet)
        self.speech = speech.Speech('вода',[set.wi // 2, set.hi - 100])
        self.u = 0
        self.text = 0
        self.image = self.wolkleft[0]
        self.rect = self.image.get_rect(center=position)
        self.rectkoll = p.Rect([self.rect.x,self.rect.y ],[self.rect.w // 4 ,self.rect.h // 3])

    def _move(self,taili,npc):
        """движение персонажа по x,y"""
        self.velocity = Vector2(0, 0)
        keys = p.key.get_pressed()
        if keys[p.K_w]:  # нажатие на клавишу w
            self.velocity.y = -1
        if keys[p.K_s]:  # нажатие на клавишу s
            self.velocity.y = 1
        if keys[p.K_a]:  # нажатие на клавишу a
            self.velocity.x = -1
        if keys[p.K_d]:  # нажатие на клавишу d
            self.velocity.x = 1
        # делаем чтобы можно было двигаться в одном направлении
        if self.velocity.length() > 1:
            self.velocity.x = 0
        self.velocity *= Player.speed
        self.rectkoll.center = self.rect.center + self.velocity * 1.5
        if self.stlok(taili) == True or self.stnpc(npc) == True:
            self.velocity.x = 0
            self.velocity.y = 0
        self.rect.center += self.velocity



    def update(self,plitki,npc):
        """обновление местоположения персонажа """
        if self.velocity.x >= 1:
            self.image = self.wolkright[self.u]
        if self.velocity.x <= -1:
            self.image = self.wolkleft[self.u]
        if self.velocity.y <= -1:
            self.image = self.wolkup[self.u]
        if self.velocity.y >= 1:
            self.image = self.wolkdown[self.u]
        if self.rect.x >= 650 and self.rect.x <= 1200 and self.rect.y >= 1000 and self.rect.y <= 1700:
            self.text = 1
        else:
            self.text = 0
            self.speech.b = 0

        if self.velocity.y != 0 or self.velocity.x != 0:
            self.u += 1
        if self.u == 4:
            self.u = 0
        self._move(plitki,npc)


    def _loadiamg(self, sheet):  # загружаем картинку персонажа

        self.wolkleft = []
        self.wolkright = []
        self.wolkup = []
        self.wolkdown = []
        w, h = sheet.w // 4, sheet.h // 4
        for x in range(0, w * 4, w):
            pr = sheet.get_image(x, 0, w, h)
            new = p.transform.scale(pr, [set.plsizenew, set.plsizenew])
            self.wolkdown.append(new)
            pr = sheet.get_image(x, h, w, h)
            new = p.transform.scale(pr, [set.plsizenew, set.plsizenew])
            self.wolkleft.append(new)
            pr = sheet.get_image(x, h * 2, w, h)
            new = p.transform.scale(pr, [set.plsizenew, set.plsizenew])
            self.wolkright.append(new)
            pr = sheet.get_image(x, h * 3, w, h)
            new = p.transform.scale(pr, [set.plsizenew, set.plsizenew])
            self.wolkup.append(new)

    def draw(self, dp, cam1):
        nwr = cam1.newrect(self.rect)
        dp.blit(self.image, nwr)
        if self.text == 1:
            self.speech.draw(dp)

        #trr = cam1.newrect(self.rectkoll)
        #p.draw.rect(dp,[0,1,0],trr)
        #print(self.rect.x)

    def stlok(self, taili):
        for u in taili:
            if u.rect.colliderect(self.rectkoll) and u.numb in set.walls:
                return True

        return False
    def stnpc(self,npc):
        if self.rectkoll.colliderect(npc.rect):
            npc.t = 0

            return True
        else:

            a = abs(npc.rect.centerx - self.rect.centerx)
            b = abs(npc.rect.centery - self.rect.centery)
            c = (a**2 + b**2) ** 0.5
            if c > 150:
                npc.speach.b = 0
                npc.t = 1
            return False


