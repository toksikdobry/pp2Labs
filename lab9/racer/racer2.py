import random, sys, pygame, time

pygame.init()

width  = 400
height = 600
step = 5
enemy_step = 10
white = (255, 255, 255)
black = (0, 0, 0)
font_size = 20
coin_step = 5
level = 1
coins_cnt = 5

font = pygame.font.SysFont("Verdana", font_size)
game_over_font = pygame.font.SysFont("Verdana", 40)
surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Street Racer")
background = pygame.image.load("AnimatedStreet.png")
clock = pygame.time.Clock()

score = 0
coins = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect  = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step)
        if(self.rect.bottom > height):
            score += 1
            self.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-step, 0)

        if self.rect.right < width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(step, 0)

        if self.rect.bottom < height:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, step)

        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -step)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, coin_step)
        if self.rect.bottom > height:
            self.rect.center = (random.randint(40, width - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (random.randint(40, width - 40), 0)

Player1 = Player()
Enemy1 = Enemy()
Coin1 = Coin()
Coin2 = Coin()
Coin3 = Coin()

coin_1 = pygame.sprite.Group()
coin_1.add(Coin1)
coin_2 = pygame.sprite.Group()
coin_2.add(Coin2)
coin_3 = pygame.sprite.Group()
coin_3.add(Coin3)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(Enemy1)



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    Player1.update()
    Enemy1.update()
    Coin1.move()

    if pygame.sprite.spritecollideany(Player1, enemy_sprites):
        surf.fill(white)
        game_over_img = game_over_font.render("GAME OVER", True, black)
        game_over_rect = game_over_img.get_rect(center = (width/2, height/2))
        surf.blit(game_over_img, game_over_rect)
        font_size = 50
        score_img  = font.render(f"Score = {score}", True, black)
        score_rect = score_img.get_rect(center = (width/2, height/2 + 50))
        surf.blit(score_img, score_rect)
        coins_img  = font.render(f"Coins = {coins}", True, black)
        coins_rect = coins_img.get_rect(center = (width/2, height/2 + 80))
        surf.blit(coins_img, coins_rect)
        pygame.display.flip()
        for entity in enemy_sprites:
            entity.kill()
        for entity in coin_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(Player1, coin_1):
        coins += 1
        Coin1.update()

    if pygame.sprite.spritecollideany(Player1, coin_2):
        coins += random.randint(1, 5)
        Coin2.update()

    if pygame.sprite.spritecollideany(Player1, coin_3):
        coins += random.randint(3, 9)
        Coin3.update()

    surf.blit(background, (0, 0))

    Enemy1.draw(surf)
    Player1.draw(surf)
    Coin1.draw(surf)

    if coins == level * coins_cnt:
        enemy_step += 2
        level += 1
    
    if level >= 2:
        Coin2.move()
        Coin2.draw(surf)

    if level >= 3:
        Coin3.move()
        Coin3.draw(surf)

    score_img = font.render(str(score), True, black)
    surf.blit(score_img, (10, 10))
    coin_img = font.render(str(coins), True, black)
    surf.blit(coin_img, (width - 30, 10))
    pygame.display.flip()
    clock.tick(60)
