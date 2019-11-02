import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My first game")

x = 50
y = 50
width = 40 # breit
height = 60  # hoch
vel = 5 # geschwindigkeit
run = True # laufen


while run: # endloss schleife (wiederholung)
    pygame.time.delay(100) # verspetung
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # gib mir alle tasten die der benutzer gedrueckt hat
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit() # beenden