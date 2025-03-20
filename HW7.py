import pygame
import datetime

#1
pygame.init()
screen = pygame.display.set_mode((680, 680))
running = True

epic_mickey_clock = pygame.image.load('C:\\Users\\Aldiy\\work\\HW7_files\\HW7_mickeyclock.jpg')
minute_hand = pygame.image.load('C:\\Users\\Aldiy\\work\\HW7_files\\HW7_minutes.png')
seconds_hand = pygame.image.load('C:\\Users\\Aldiy\\work\\HW7_files\\HW7_seconds.png')

EMC_rect = epic_mickey_clock.get_rect(center=(340, 340))
MH_rect = minute_hand.get_rect(center=(340, 340))
SH_rect = seconds_hand.get_rect(center=(340, 340))

start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    rotating_MH = pygame.transform.rotate(minute_hand,  -5.9 * minutes)
    rotating_SH = pygame.transform.rotate(seconds_hand, -5.9 * seconds)
    MH_rect_r = rotating_MH.get_rect(center=(340, 340))
    SH_rect_r = rotating_SH.get_rect(center=(340, 340))

    screen.blit(epic_mickey_clock, EMC_rect)
    screen.blit(rotating_MH, MH_rect_r)
    screen.blit(rotating_SH, SH_rect_r)

    pygame.display.flip()
pygame.quit()

#2
pygame.init()
