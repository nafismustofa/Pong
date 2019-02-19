import pygame , random

class Game:
    #Variables
    __is_running = True
    __is_paused = False
    __FPS = 60
    __screen_size = (__screen_width , __screen_height) = (800 , 600)
    
    #Colors
    __color_black = (0 , 0 , 0)
    __color_white = (255 , 255 , 255)
    __color_blue = (0 , 0 , 255)
    __color_red = (255 , 0 , 0)

    #Player Variables
    __start_with_player_1 = True

    #Paddles Variables
    __left_paddle_y = (__screen_height // 2) - 50
    __right_paddle_y = (__screen_height // 2) - 50

    #Ball Variables
    __ball_x = __screen_width // 2
    __ball_y = __screen_height // 2
    if __start_with_player_1 == True:
        __ball_speed = [-4 , random.choice([4 , -4])]
    else:
        __ball_speed = [4 , random.choice([4 , -4])]

    #Objects
    __game_display = None
    __clock = pygame.time.Clock()

    #Paddles Function
    def __paddles(self):
        pygame.draw.rect(self.__game_display , self.__color_red , [10 , self.__left_paddle_y , 20 , 100]) #Left Paddle
        pygame.draw.rect(self.__game_display , self.__color_blue , [(self.__screen_width - 30) , self.__right_paddle_y , 20 , 100]) #Right Paddle

    #Ball Function
    def __ball(self):
        #Draw Ball
        pygame.draw.circle(self.__game_display , self.__color_white , (self.__ball_x , self.__ball_y) , 15)

        #Move Ball
        self.__ball_x += self.__ball_speed[0]
        self.__ball_y += self.__ball_speed[1]

        #Collision Check
        if (self.__ball_y - 15) < 0 or (self.__ball_y + 15) > self.__screen_height:
            self.__ball_speed[1] = -self.__ball_speed[1]

    #Main Display Function
    def game(self):
        #Pygame Initialization
        pygame.init()

        #Display Setup
        self.__game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("PONG")

        #Main Game Loop
        while self.__is_running:
            #Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False
                #Input Event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.__is_paused == False:
                            self.__is_paused = True
                        else:
                            self.__is_paused = False

            #Set Background Color
            self.__game_display.fill(self.__color_black)

            #Initialize Paddles
            self.__paddles()

            #Initialize Ball
            self.__ball()

            #Display Update
            if self.__is_paused == False:
                pygame.display.update()

            #Set FPS
            self.__clock.tick(self.__FPS)
        
        #Quiting Functions
        pygame.quit()
        quit()