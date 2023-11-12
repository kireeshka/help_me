import pygame as p
from set import *
from player import Player
from helper import res
import cam
import npc
import map
p.init()
class Main():
    def __init__(self):
        self.clock = p.time.Clock()
        self.runing = True
        """цикл работы игры"""
        self.dp = p.display.set_mode((wi, hi))
        p.display.set_caption(game_name)
        p.display.set_icon(p.image.load(res / 'spite' / 'image.png'))  # добавляем иконку для игры
        self.pl = Player(res / 'spite' / 'player.png', (1900, 2000))  # добавляем спрайт персонажа
        self.all_sprites = p.sprite.Group()  # группа для спрайтов
        self.all_sprites.add(self.pl)
        self.maps = map.Map('carta..csv')
        self.cam1 = cam.Cam()
        self.npc = npc.NPC((1900,1800),self.maps.spritesformap[122])

    def __Events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.runing = False
    def __draw(self):
        self.dp.fill((255, 255, 255))
        self.maps.draw(self.dp,self.cam1)
        self.npc.draw(self.dp,self.cam1)
        self.pl.draw(self.dp, self.cam1)

    def __update(self):
        self.pl.update(self.maps.listwithspr,self.npc)
        self.cam1.shpion(self.pl,self.maps)
        self.npc.update()
        self.clock.tick(fps)
        p.display.flip()
    def run(self):
        while self.runing:
            self.__Events()
            self.__draw()
            self.__update()
game = Main()
game.run()






