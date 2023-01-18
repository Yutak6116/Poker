import pygame,sys, random , copy , collections
from pygame.locals import *

your_turnrect = Rect(460, 520, 80, 20)
text_your_turn = "Your Turn"

font2 = pygame.font.SysFont(None, 20) #他で定義していれば不要
text_your_turn = font2.render(text_your_turn, True, (0,0,0))

if #playerのターン　:
    pygame.draw.rect(screen, white ,your_turnrect)
    screen.blit(text_your_turn, text_your_turn.get_rect(center=(500,530)))
else:
    pygame.draw.rect(screen, green ,your_turnrect)
 

