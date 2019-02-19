import pygame

class Display:
    #Variables
    __is_runnning = True
    __FPS = 60
    __screen_size = (screen_width , screen_height) = (800 , 600)
    
    #Colors
    __color_black = (0 , 0 , 0)
    __color_white = (255 , 255 , 255)

    #Paddles Variables
    left_paddle_y = (screen_height // 2) - 50
    right_paddle_y = (screen_height // 2) - 50

    #Objects
    __game_display = None
    __clock = pygame.time.Clock()

    #Draw Paddles Function
    def __draw_paddles(self):
        pygame.draw.rect(self.__game_display , self.__color_white , [10 , self.left_paddle_y , 20 , 100]) #Left Paddle
        pygame.draw.rect(self.__game_display , self.__color_white , [(self.screen_width - 30) , self.left_paddle_y , 20 , 100]) #Left Paddle

    #Main Display Function
    def display(self):
        #Pygame Initialization
        pygame.init()

        #Display Setup
        self.__game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("PONG")

        #Main Game Loop
        while self.__is_runnning:
            #Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_runnning = False
            
            #Set Background Color
            self.__game_display.fill(self.__color_black)

            #Draw Paddles
            self.__draw_paddles()

            #Display Update
            pygame.display.update()

            #Set FPS
            self.__clock.tick(self.__FPS)
        
        #Quiting Functions
        pygame.quit()
        quit()