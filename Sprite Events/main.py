import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Pygame Sprite!")

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/spaceship_red.png")
        self.image = pygame.transform.scale(self.image, (50,45))
        self.rect = self.image.get_rect()
        
    def move_ship(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:
            self.rect.move_ip(0,-20)
        elif keys_pressed[pygame.K_DOWN]:
            self.rect.move_ip(0,20)
        elif keys_pressed[pygame.K_LEFT]:
            self.rect.move_ip(-20,0)
        elif keys_pressed[pygame.K_RIGHT]:
            self.rect.move_ip(20,0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            

# creating a group for sprites

sprite_group = pygame.sprite.Group()

def start_game():
    ship = Ship()
    sprite_group.add(ship)
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        # getting the set of keys pressed 
        keys_pressed = pygame.key.get_pressed()
        ship.move_ship(keys_pressed)
        bg = pygame.image.load("./images/spacebg.png")
        screen.blit(bg, (0,0))
        sprite_group.draw(screen)
        pygame.display.update()

start_game()