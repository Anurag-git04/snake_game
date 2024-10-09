import pygame
import random

pygame.init()

#color
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,0)

#game variables
running=True
game_over=False

fps=30
clock=pygame.time.Clock()

screen_width=600
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My_CAr_Game")



    
def gameloop():
    running=True
    game_over=False
    
    snake_x=15
    snake_y=0
    snake_size=25
    velocity_x=0 
    velocity_y=0
    init_velocity=5

    food_x=random.randint(20, screen_width-20)
    food_y=random.randint(20, screen_height-20)

    score=0
    
    snk_list=[]
    snk_length=1
    
    def plot_snake(gamewindow,black,snk_list,snk_size):
        print(snk_list)
        for x,y in snk_list:
            pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])

    while running:
        if game_over:
            running=False
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
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

        snake_x=snake_x+velocity_x
        snake_y=snake_y+velocity_y
        
        if(abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10):
            score+=1
            print(score)
            food_x=random.randint(20, screen_width-20)
            food_y=random.randint(20, screen_height-20)
            snk_length=snk_length+10
        
        if (snake_x<0 or snake_y<0 or snake_y>screen_height or snake_x>screen_width):
            running=False
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)
        
        if (len(snk_list)>snk_length):
            del snk_list[0]
        
        if(head in snk_list[::-1]):
            game_over=True
                    
        gamewindow.fill(white)
        pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
        plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
gameloop()