# tut 12 & 13
import pygame
import random
pygame.init()

#color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=600
screen_height=880
gamewindow=pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption("Snake Game With Anurag")

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
fps=60


clock=pygame.time.Clock()
#Game loop

while not exit_game:
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
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y
    
    if abs(snake_x-food_x)<6 and abs (snake_y-food_y)<6:
        score+=1
        print("Score:",score)
        food_x=random.randint(20, screen_width/2)
        food_y=random.randint(30, screen_height/2)

    
    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()