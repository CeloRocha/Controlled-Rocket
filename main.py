import pygame
from globalVariables import (
    X_PIXELS, 
    Y_PIXELS,
    SETPOINT,
    Y_METROS,
    GREEN,
    RED
)
from utils import *
from rocket import Rocket

pygame.init()
clock = pygame.time.Clock()
continueRunning = True

screen = pygame.display.set_mode((X_PIXELS, Y_PIXELS))
pygame.display.set_caption('Foguete controlado')

font = pygame.font.SysFont(None, 24)
img = font.render('', True, GREEN)
rect = img.get_rect()
rect.topleft = (40, 30)
lineHeight = 120

rocket = Rocket()
setHeight = yMetersToPixels(SETPOINT)

while continueRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueRunning = False
        if event.type == pygame.MOUSEBUTTONUP:
            _, mouse_y = pygame.mouse.get_pos()
            rocket.setTarget(yPixelsToMeters(mouse_y))
            setHeight = mouse_y
    screen.fill(pygame.Color("black"))
    img = font.render(f'Alvo: {Y_METROS - int(yPixelsToMeters(setHeight))}[m], Velocidade: {-rocket.get_dy()*100//1/100}[m/s]', True, GREEN)
    rect.size=img.get_size()
    screen.blit(img, rect)
    pygame.draw.line(screen, RED, (0, setHeight), (X_PIXELS, setHeight), width=2)
    rocket.update(clock.get_time()/1000)
    rocket.draw(screen)
    clock.tick(60)
    pygame.display.update()