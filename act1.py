import pygame

pygame.init

screen=pygame.display.set_mode((500,500))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen, (252, 186, 3), pygame.Rect(40,387,200,90))

    pygame.display.flip()