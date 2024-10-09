import pygame
pygame.init()

#creating window
gamewindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

#game specific variable
exit_game=False
game_over=False


# creating a gameloop
while not exit_game:
    # creeating and understanding event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You have press right arrow key")
        

pygame.quit()
quit()