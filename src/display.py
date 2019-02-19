import pygame
from player_input import Player_Input

class Display:
    #Variables
    __is_running = True
    __FPS = 60
    __screen_size = (__screen_width , __screen_height) = (800 , 600)

    #Colors
    __color_black = (0 , 0 , 0)
    __color_white = (255 , 255 , 255)

    #Objects
    __clock = pygame.time.Clock()
    __player_input = Player_Input()

    #Main Display Function
    def display(self):
        #Pygame Initializations
        pygame.init()

        #Display Setup
        game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("PONG")

        #Main Game Loop
        while self.__is_running:
            #Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running == False
            while self.__player_input.is_paused:
                
                