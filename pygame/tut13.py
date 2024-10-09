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

food_x=random.randint(0, screen_width)
food_y=random.randint(0, screen_height)

snake_size=15
fps=30


clock=pygame.time.Clock()
#Game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=5
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-5
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-5
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=5
                velocity_x=0
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()