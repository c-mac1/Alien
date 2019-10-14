import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet'''

    def __init__(self, ai_settings, screen):
        '''Initialise alien and set starting pos'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien 
        self.image = pygame.image.load(r'part2\project1_alien\images\alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien at top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens pos
        self.x = float(self.rect.x)

    
    def check_edges(self):
        '''Return True if the alien is at the edge'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Move alien right (as it comes from the left)'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    


    def blitme(self):
        self.screen.blit(self.image, self.rect)