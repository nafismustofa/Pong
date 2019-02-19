import pygame

class Player_Input:
    #Variables
    is_paused = False

    #Main Input Function
    def player_input(self):
        input_key = pygame.key.get_pressed()

        if input_key[pygame.K_SPACE]:
            is_paused = True