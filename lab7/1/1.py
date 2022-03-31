import pygame
import datetime


def rotat(surf, image, angle, pos, originPos):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)


pygame.init()
w = 1300
h = 975
pivotPos       = [w/2, h/2]
originPosRight = [160, 140]
originPosLeft  = [10, 150]

screen = pygame.display.set_mode((w, h))
clock  = pygame.time.Clock()
clockimg = pygame.image.load('clock.jpg')
rightimg = pygame.image.load('righthand.png') # 180x155
leftimg  = pygame.image.load('lefthand.png') # 245x163

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key:
            if event.key == pygame.K_ESCAPE:
                done = True
    
    secAngle = (datetime.datetime.now().second / 60) * 360
    minAngle = (datetime.datetime.now().minute / 60) * 360

    screen.fill((255, 255, 255))
    screen.blit(clockimg, (0, 0))
    rotat(screen, rightimg, minAngle + 48,  pivotPos, originPosRight)
    rotat(screen, leftimg,  secAngle - 57,  pivotPos, originPosLeft )
    
    pygame.draw.circle(screen, (232, 34, 51), pivotPos, 20)
    pygame.display.flip()
    clock.tick(60)