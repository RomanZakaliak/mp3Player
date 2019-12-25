import pygame

class player(object):
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pyGMix = pygame.mixer
    pyGMix.init()
    endEvent = pygame.USEREVENT+1
    pygame = pygame
    def setFile(self, filename:str):
        self.pyGMix.music.load(filename)

    def __del__(self):
        self.pyGMix.quit()


