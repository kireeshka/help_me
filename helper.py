import pygame as p
import sys
from pathlib import Path


class Sprite_sheet:
    def __init__(self, file_paf):
        """загружает лист спрайта по заданому пути"""
        self.sheet = p.image.load(file_paf).convert_alpha()

    def get_image(self, x, y, width, height):
        """работа с листом спрайта"""
        return self.sheet.subsurface(x, y, width, height)
#облегчение доступа к ресурсам
res = Path(sys.argv[0]).parent/"res"