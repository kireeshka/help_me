import pygame as p
import  helper
import set
class Map():
    def __init__(self, csvname):
        self.csvname = csvname
        filecarti = open(csvname, 'r')
        dkod = filecarti.readlines()
        self.listmapcsv = []
        self.listwithspr = []
        for i in dkod:
            s = i.split(',')
            self.listmapcsv.append(s)
        self.spritesformap = []
        self.images()
        self.plitki()
        self.strr = len(self.listmapcsv)
        self.strr *= set.sizenew
        self.width = len(self.listmapcsv[1])
        self.width *= set.sizenew


    def images(self):
        a = helper.Sprite_sheet('ppg_tileset.png')
        for u in range(8):
            u = u * set.sizesprorig
            for i in range(17):
                i = i * set.sizesprorig
                kartinka = a.get_image(i,u,set.sizesprorig,set.sizesprorig)
                kartinka = p.transform.scale(kartinka,[set.sizenew,set.sizenew])
                self.spritesformap.append(kartinka)
    def plitki(self):
        for l in range(len(self.listmapcsv)):
            p = self.listmapcsv[l]
            for o in range(len(p)):
                e = int(p[o])
                n = self.spritesformap[e]
                y = l * set.sizenew
                x = o * set.sizenew
                plitka = Plitki([x,y],n,e)
                self.listwithspr.append(plitka)
    def draw(self,dp,cam1):
        for k in self.listwithspr:
            k.draw(dp,cam1)




class Plitki():
    def __init__(self,pos,imag,numb):
        self.pos = pos
        self.imag = imag
        self.rect = p.Rect(self.pos,[set.sizenew,set.sizenew])
        self.numb = numb
    def draw(self, dp,cam1):
        newr = cam1.newrect(self.rect)
        dp.blit(self.imag,newr)







