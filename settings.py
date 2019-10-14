class Settings():
    ''' A class to store settings for the alien invasion game'''


    def __init__(self):
        '''Initilaise gams static settings'''
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3


        #Alien setting
        self.fleet_drop_speed = 10
        

        #how quickly the game speeds 
        self.speedup_scale =1.5

        #alien point increase
        self.score_scale = 1.5



        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    
    def increase_speed(self):
        '''increses game speed'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)