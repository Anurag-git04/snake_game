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

#Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            exit_game=True

    gamewindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()