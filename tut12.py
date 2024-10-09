# tut 12 & 13
import pygame
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
velocity_x=1
velocity_y=1
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
                snake_x=snake_x+10
            if event.key==pygame.K_LEFT:
                snake_x=snake_x-10
            if event.key==pygame.K_UP:
                snake_y=snake_y-10
            if event.key==pygame.K_DOWN:
                snake_y=snake_y+10
                
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()