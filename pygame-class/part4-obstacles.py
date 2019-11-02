import pygame

pygame.init()

screen_width = 1028
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game")
path = 'resources/background'
bgs = [pygame.image.load(path + '/bg_3.png'), pygame.image.load(path + '/bg_2.png'), pygame.image.load(path + '/bg_1.png'), pygame.image.load(path + '/bg_0.png')]
cactus = pygame.transform.scale(pygame.image.load('resources/cactus/cactus_1.png'), (80, 80))
hero = pygame.image.load('resources/R1.png')

clock = pygame.time.Clock()


x = 50
y = 550
width = 64
height = 64
vel = 30
run = True
isJump = False
jumpHight = 8
jumpCount = jumpHight
obstacles = []
bgX = 0
cactusX = 600


def draw():
    global bgX
    bgX -= 1
    screen.fill((255, 255, 255))
    for bg in bgs:
        screen.blit(pygame.transform.scale(bg, (screen_width, screen_height)), (0, 0))
    pygame.display.update()

def draw_hero():
    screen.blit(hero, (x, y))
    pygame.display.update()

def obstacles():
    global cactusX
    screen.blit(cactus, (cactusX, 550))
    cactusX -= vel
    if(cactusX < 0):
        cactusX = screen_width
    pygame.display.update()

def collision():
    if (x < cactusX + 80 and x + width > cactusX and y < 630 and y + height > 550):
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, width, height))
    pygame.display.update()



while run:
    clock.tick(10)
    draw()
    draw_hero()
    obstacles()
    collision()

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < screen_width - width:
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

pygame.quit()