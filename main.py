import pygame as p
from set import *
from player import Player
from helper import res

p.init()
clock = p.time.Clock()
dp = p.display.set_mode((wi, hi))
p.display.set_caption(game_name)
p.display.set_icon(p.image.load(res/'spite'/'image.png')) #добавляем иконку для игры
pl = Player(res/'spite'/'player.png', (100, 100)) # добавляем спрайт персонажа
all_sprites = p.sprite.Group() # группа для спрайтов
all_sprites.add(pl)
runing = True
"""цикл работы игры"""
while runing:
    for event in p.event.get():
        if event.type == p.QUIT:
            runing = False
    pl.update()
    dp.fill((255, 255, 255))
    all_sprites.draw(dp)
    clock.tick(fps)
    p.display.flip()

