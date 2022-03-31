import pygame

pygame.init()
w = 300
h = 300
screen = pygame.display.set_mode((w, h))
clock  = pygame.time.Clock()
pygame.display.set_caption("Yelaman's player")

songs = ["A_Cruel_Angels_Thesis.mp3", "Centimeter.mp3", "Miss_The_Rage.mp3", "Mister_718.mp3", "Praise_the_lord.mp3"]

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            songs = songs[1:] + [songs[0]]
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            songs = [songs[-1]] + songs[:-1]
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pygame.mixer.music.unpause()
    
    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)