# tut 12 & 13
from numpy import true_divide
import pygame
import random
import os


pygame.mixer.init()
pygame.init()

#color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=500
screen_height=800
gamewindow=pygame.display.set_mode((screen_height,screen_width))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game With Anurag")

#background image
bgimg=pygame.image.load("snk_background.png")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()


font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
        # print(snk_list)
        for x,y in snk_list:
            pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])
def gameloop():
    #game variable
    exit_game=False
    game_over=False
    snake_x=25
    snake_y=0
    velocity_x=0
    velocity_y=0
    init_velocity=5

    score=0

    food_x=random.randint(20, screen_width/2)
    food_y=random.randint(30, screen_height/2)

    snake_size=15
    fps=40
    #check if file exist or not
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt",'w') as f:
            f.write("0")
    with open("hiscore.txt",'r') as f:
        hiscore=f.read()
    
    clock=pygame.time.Clock()
    #Game loop
    snk_list=[]
    snk_length=1 

    

    while not exit_game:
        if game_over:
            with open("hiscore.txt",'w') as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Game Over !!!!! Enter to play again!!!",red,30,120)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=10
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            
            if abs(snake_x-food_x)<6 and abs (snake_y-food_y)<6:
                score+=10
                snk_length+=5
                food_x=random.randint(20, screen_width/2)
                food_y=random.randint(30, screen_height/2)
                pygame.mixer.music.load('snk.mp3')
                pygame.mixer.music.play()
                if score>int(hiscore):
                    hiscore=score
            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score:"+ str(score) + " Hiscore:" + str(hiscore),red,5,5)
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()
                # print("Game over")
            
            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                game_over=True 
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()   

            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            #pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
# gameloop()
def welcome():
    exit_game=False
    pygame.mixer.music.load('epic_battle.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gamewindow.fill((225,219,230))
        gamewindow.blit(bgimg,(0,0))
        text_screen("Welcome TO game!!!!",black,190,200)
        text_screen("press spacebar to play the game",black,100,240) 
        
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(40)
welcome()
