import pygame

pygame.init()

screen = pygame.display.set_mode((500, 480))
pygame.display.set_caption("My first game")
bg = pygame.image.load('resources/bg2.png')
hero = pygame.image.load('resources/R1.png')


x = 50
y = 365
width = 64
height = 64
vel = 10
run = True
isJump = False
jumpHight = 8
jumpCount = jumpHight

bgX = 0

screen.fill((255, 255, 255))
pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
pygame.display.update()

while run:
    pygame.time.delay(10)
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True 
    else:
        if jumpCount >= -jumpHight:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = jumpHight

    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(bg, (500, 520)) , (bgX, 0))
    screen.blit(pygame.transform.scale(bg, (500, 520)) , (bgX + 220,0))
    bgX -= 1
    screen.blit(hero, (x, y))
    pygame.display.update()


pygame.quit()