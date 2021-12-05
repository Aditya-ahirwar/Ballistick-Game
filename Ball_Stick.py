import pygame
import random
from pygame.constants import K_RIGHT

pygame.init()

# creating game window 
window_width = 500
window_height = 600
game_window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Ball And Stick")

clock = pygame.time.Clock()
red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
font = pygame.font.SysFont(None,40)

# defining functions to print message

def PrintMsg():
    screen_text = font.render("Game Over Press Enter!!",True,red)
    game_window.blit(screen_text,[100,250])

# game loop 

def GameLoop():
    # creating game variables
    ball_x = random.randint(50,250)
    ball_y = 10
    ball_size = 10
    stick_x = window_width/2
    stick_y = window_height - 50
    stick_length = 50
    stick_height = 10
    svx = 0
    bvx = 5
    bvy = 5
    EndGame = False
    Retry = False
    fps = 60
    while not EndGame:
        if Retry:
            PrintMsg()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GameLoop()
                if event.type == pygame.QUIT:
                    EndGame = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    EndGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        svx = 5
                    if event.key == pygame.K_LEFT:
                        svx = -5

        if ball_x <= 0 or ball_x >= 500:
            bvx = -1*(bvx)
        if ball_y <= 0:
            bvy = -1*(bvy)
        if ball_y >= 600:
            bvy = -1*(bvy)
            # Retry = True
        if abs(ball_x - stick_x)<=25 and abs(stick_y - ball_y)<= 5:
            bvy = -1*(bvy)
        if stick_x <=0 or stick_x >=500:
            svx = -1*(svx)

        ball_x = ball_x + bvx
        ball_y = ball_y + bvy
        stick_x += svx
        game_window.fill(white)
        # pygame.draw.rect(game_window,red,[ball_x,ball_y,ball_size,ball_size])
        pygame.draw.circle(game_window, red,(ball_x,ball_y),7)
        pygame.draw.rect(game_window, black,[stick_x, stick_y, stick_length, stick_height])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

GameLoop()


