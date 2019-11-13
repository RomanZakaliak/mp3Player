import pygame

class player(object):
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pyGMix = pygame.mixer
    pyGMix.init()

    def getFile(self, filename:str):
        self.pyGMix.music.load(filename)

