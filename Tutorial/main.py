import pygame, sys

pygame.init()

HEIGHT, WIDTH = 600, 1000
display = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

# Background
background = pygame.transform.scale(pygame.image.load('images/background.png').convert_alpha(), (WIDTH, HEIGHT))

#Caption
pygame.display.set_caption('My game')

# Icon
icon = pygame.image.load('icon.png').convert_alpha()
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Rect
rect = pygame.Rect(0, 0, 50, 50)

# Surface
surface = pygame.Surface((80, 80))
surface.fill((200, 200, 200))

# Alien Surface
alien_png = pygame.image.load('alien.png').convert_alpha()
alien = pygame.transform.scale(alien_png, (64, 64)) # scale the alien_png
alien_rect = alien.get_rect(topleft = (200, 100))

# Class Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.idle_sprites = [pygame.image.load(f'images/idle_{img}.png') for img in range(1, 9)]
        self.running_right_sprites = [pygame.image.load(f'images/run_{img}.png') for img in range(1, 9)]
        self.running_left_sprites = [pygame.transform.rotate(pygame.image.load(f'images/run_{img}.png'), -180) for img in range(1, 9)]
        self.current_sprite = 0
        self.image = self.idle_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        self.time = 0

        self.standing = True
        self.running_right = False
        self.running_left = False

    def update(self):
        self.time += 1

        if self.time == 6:
            self.current_sprite += 1
            self.time = 0

        if self.standing == True:
            if self.current_sprite < len(self.idle_sprites):
                self.image = self.idle_sprites[self.current_sprite]
            else:
                self.current_sprite = 0
        elif self.running_right == True:
            if self.current_sprite < len(self.running_right_sprites):
                self.image = self.running_right_sprites[self.current_sprite]
            else:
                self.current_sprite = 0
        elif self.running_left == True:
            if self.current_sprite < len(self.running_left_sprites):
                self.image = self.running_left_sprites[self.current_sprite]
            else:
                self.current_sprite = 0

    def get_input_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.standing = False
            self.running_right = True
            self.running_left = False
            self.rect.x += 4
        elif keys[pygame.K_LEFT]:
            self.standing = False
            self.running_right = False
            self.running_left = True
            self.rect.x -= 4
        elif keys[pygame.K_DELETE]:
            self.kill()
        else:
            self.standing = True
            self.running_right = False
            self.running_left = False

    def come_back(self):
        if self.rect.x > WIDTH + self.rect.width:
            self.rect.x = 0 - self.rect.width

        elif self.rect.x < 0 - self.rect.width:
            self.rect.x = WIDTH + self.rect.width

moving_sprites = pygame.sprite.Group()
player = Player(300, 300)
moving_sprites.add(player)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill((30, 30, 30))
    display.blit(background, (0, 0))

    pygame.draw.rect(display, (200, 200, 200), rect, 2)
    display.blit(surface, (100, 160))

    # Drawing the Alien
    display.blit(alien, (alien_rect.x, alien_rect.y))

    # Player Drawing
    moving_sprites.draw(display)
    player.get_input_keys()
    player.come_back()
    moving_sprites.update()
    print(player.rect.width, player.rect.height)

    pygame.display.update()
    clock.tick(60)