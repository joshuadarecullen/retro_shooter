import pygame
import json


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')

        # load in sprite sheet from disk
        try:
            with open(self.meta_data) as f:
                self.data = jsonload(f)
        except e:
            print(f'{e}')


    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        # sprite.set_colorkey((0,0,0)) # deals with transparency in sprites

        # arguements: where its from, align, tells where and how big the image
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h)) 

        return sprite

    def parsed_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
