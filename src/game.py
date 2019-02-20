import pygame , random

class Game:
    def __init__(self):
        #Variables
        self.__is_running = True
        self.__is_paused = False
        self.__FPS = 60
        self.__screen_size = (self.__screen_width ,self. __screen_height) = (800 , 600)
    
        #Colors
        self.__color_black = (0 , 0 , 0)
        self.__color_white = (255 , 255 , 255)
        self.__color_blue = (0 , 0 , 255)
        self.__color_red = (255 , 0 , 0)

        #Player Variables
        self.__start_with_player_1 = True
        self.__player_1_score = 0
        self.__player_2_score = 0

        #Paddles Variables
        self.__left_paddle_y = (self.__screen_height // 2) - 50
        self.__right_paddle_y = (self.__screen_height // 2) - 50

        #Ball Variables
        self.__ball_x = self.__screen_width // 2
        self.__ball_y = self.__screen_height // 2
        if self.__start_with_player_1 == True:
            self.__ball_speed = [-4 , random.choice([4 , -4])]
        else:
            self.__ball_speed = [4 , random.choice([4 , -4])]

        #Objects
        self.__game_display = None
        self.__clock = pygame.time.Clock()
        self.__icon = pygame.image.load("./assets/pong_icon.png")

    #Paddles Function
    def __paddles(self):
        pygame.draw.rect(self.__game_display , self.__color_red , [10 , self.__left_paddle_y , 20 , 100]) #Left Paddle
        pygame.draw.rect(self.__game_display , self.__color_blue , [(self.__screen_width - 30) , self.__right_paddle_y , 20 , 100]) #Right Paddle

        #Border Check
        if self.__left_paddle_y <= 7:
            self.__left_paddle_y += 10
        if self.__left_paddle_y >= (self.__screen_height - 107):
            self.__left_paddle_y -= 10
        if self.__right_paddle_y <= 7:
            self.__right_paddle_y += 10
        if self.__right_paddle_y >= (self.__screen_height - 107):
            self.__right_paddle_y -= 10

    #Ball Function
    def __ball(self):
        #Draw Ball
        pygame.draw.circle(self.__game_display , self.__color_white , (self.__ball_x , self.__ball_y) , 15)

        #Move Ball
        self.__ball_x += self.__ball_speed[0]
        self.__ball_y += self.__ball_speed[1]

        #Border Collision Check
        if (self.__ball_y - 15) < 0 or (self.__ball_y + 15) > self.__screen_height:
            self.__ball_speed[1] = -self.__ball_speed[1]
        if (self.__ball_x - 15) <= 0:
            self.__player_2_score += 1
            self.__start_with_player_1 = True
            self.__ball_x = self.__screen_width // 2
            self.__ball_y = self.__screen_height // 2
        if (self.__ball_x + 15) >= self.__screen_width:
            self.__player_1_score += 1
            self.__start_with_player_1 = False
            self.__ball_x = self.__screen_width // 2
            self.__ball_y = self.__screen_height // 2

        #Paddle Collision Check
        if(self.__ball_x - 15) <= 30 and (self.__ball_y >= self.__left_paddle_y and self.__ball_y <= (self.__left_paddle_y + 100)):
            self.__ball_speed[0] = -self.__ball_speed[0]
        if(self.__ball_x + 15) >= (self.__screen_width - 30) and (self.__ball_y >= self.__right_paddle_y and self.__ball_y <= (self.__right_paddle_y + 100)):
            self.__ball_speed[0] = -self.__ball_speed[0]
    
    #Text Display
    def __text(self):
        #Fonts
        title_font = pygame.font.SysFont(None , 30)
        score__font = pygame.font.SysFont(None , 20)

        #Title Text
        title = title_font.render("PONG" , True , self.__color_white)
        title_rect = title.get_rect()
        title_rect.centerx = (self.__screen_width // 2)
        title_rect.centery = 30

        #Player 1 Score Text
        player_1_score = score__font.render("Player 1 : {}" .format(self.__player_1_score) , True , self.__color_red)
        player_1_score_rect = player_1_score.get_rect()
        player_1_score_rect.centerx = 100
        player_1_score_rect.centery = 50

        #Player 2 Score Text
        player_2_score = score__font.render("Player 2 : {}" .format(self.__player_2_score) , True , self.__color_blue)
        player_2_score_rect = player_2_score.get_rect()
        player_2_score_rect.centerx = (self.__screen_width - 100)
        player_2_score_rect.centery = 50

        #Display Texts
        self.__game_display.blit(title , title_rect)
        self.__game_display.blit(player_1_score , player_1_score_rect)
        self.__game_display.blit(player_2_score , player_2_score_rect)

    #Input Function
    def __input(self):
        input_key = pygame.key.get_pressed()

        if input_key[pygame.K_w]:
            self.__left_paddle_y -= 10
        if input_key[pygame.K_s]:
            self.__left_paddle_y += 10
        if input_key[pygame.K_UP]:
            self.__right_paddle_y -= 10
        if input_key[pygame.K_DOWN]:
            self.__right_paddle_y += 10

    #Main Display Function
    def game(self):
        #Pygame Initialization
        pygame.init()

        #Display Setup
        self.__game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("PONG")
        pygame.display.set_icon(self.__icon)

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

            #Pause Trigger
            if self.__is_paused == False:
                #Game Input
                self.__input()
                
                #Set Background Color
                self.__game_display.fill(self.__color_black)

                #Display Text
                self.__text()

                #Display Paddles
                self.__paddles()

                #Display Ball
                self.__ball()

                #Screen Update
                pygame.display.update()

                #FPS Setup
                self.__clock.tick(self.__FPS)
            
        #Quiting Functions
        pygame.quit()
        quit()
