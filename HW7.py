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
pygame.mixer.init()
running = True

current_song = 0
song_names = ["Current song: Фата", "Current song: Аспанға Қараймын", "Current song: Шудың Бойында", "Current song: ???"]
songs = ["C:\\Users\\Aldiy\\work\\HW7_files\\Улангасыр Ками - Фата.mp3", "C:\\Users\\Aldiy\\work\\HW7_files\\Бегей - Аспанга караймын.mp3", "C:\\Users\\Aldiy\\work\\HW7_files\\Ахан Отыншиев - Шудын бойында.mp3", "C:\\Users\\Aldiy\\work\\HW7_files\\25. Bath Hall.mp3"]
screen = pygame.display.set_mode((480, 200))

font = pygame.font.SysFont("arial", 15)
text1 = font.render('To play the song, press 1.', True, (255, 255, 255))
text2 = font.render('To stop the song, press 2.', True, (255, 255, 255))
text3 = font.render('To select next song, press W.', True, (255, 255, 255))
text4 = font.render('To select previous song, press Q.', True, (255, 255, 255))

song_font = pygame.font.SysFont("arial", 20)

pygame.mixer.music.load(songs[current_song])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                current_song = (current_song + 1) % 4
                pygame.mixer.music.load(songs[current_song])
            if event.key == pygame.K_q:
                current_song = (current_song - 1) % 4
                pygame.mixer.music.load(songs[current_song])
            if event.key == pygame.K_1:
                pygame.mixer.music.play()
            if event.key == pygame.K_2:
                pygame.mixer.music.stop()

    screen.fill((0, 0, 0))
    screen.blit(text1, (0, 0))
    screen.blit(text2, (0, 15))
    screen.blit(text3, (0, 30))
    screen.blit(text4, (0, 45))

    song_text = song_font.render(song_names[current_song], True, (255, 255, 0))
    screen.blit(song_text, (0, 100))

    pygame.display.flip()

pygame.quit()

#3
pygame.init()
screen = pygame.display.set_mode((160, 160))
running = True
x = 80
y = 80

clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 20: y -= 20
        if pressed[pygame.K_DOWN] and y < 150: y += 20
        if pressed[pygame.K_LEFT] and x > 20: x -= 20
        if pressed[pygame.K_RIGHT] and x < 150: x += 20
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 25)
        
        pygame.display.flip()
        clock.tick(60)

pygame.quit()