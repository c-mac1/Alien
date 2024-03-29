import pygame
from pygame.sprite import Sprite


class Ship(Sprite):


    def __init__(self, ai_settings, screen):
        '''Initialise the ship and set its starting posotion'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load image
        self.image = pygame.image.load('part2/project1_alien/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start ship at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal val for ships center
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''Updtes ship position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def center_ship(self):
        self.center = self.screen_rect.centerx


    def blitme(self):
        '''Draw ship at currrent location'''
        self.screen.blit(self.image, self.rect)