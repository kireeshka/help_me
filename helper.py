import pygame as p
import sys
from pathlib import Path


class Sprite_sheet:
    def __init__(self, file_paf, scale = 1):
        """загружает лист спрайта по заданому пути"""
        sheet = p.image.load(file_paf).convert_alpha()
        w,h = sheet.get_size()
        targetsize = (int(w * scale), int (h * scale))
        self.sheet = p.transform.scale(sheet,targetsize)
        self.w, self.h = self.sheet.get_size()

    def get_image(self, x, y, width, height):
        """работа с листом спрайта"""
        return self.sheet.subsurface(x, y, width, height)

#облегчение доступа к ресурсам
res = Path(sys.argv[0]).parent/"res"