import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My first game")

x = 50
y = 540
width = 40
height = 60
vel = 10
run = True
isJump = False
jumpCount = 10


while run:
    pygame.time.delay(10)
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 600 - width:
        x += vel
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if not isJump:
        if keys[pygame.K_UP] and  y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 600 - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()