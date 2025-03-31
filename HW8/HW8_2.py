#2
import pygame
import random
import sys
 
pygame.init()
 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Demo")
clock = pygame.time.Clock()
 
#Game Font
font = pygame.font.Font(None,30)
 
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 100, 100)
D_PINK = (120, 20, 20)
PURPLISH = (255, 100, 255)
D_PURPLISH = (120, 20, 120)

#Level variable
level = 0
 
# Snake Settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15
 
# Food settings
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Adding "Perishables", dissapearing food (Lab 9)
peri_pos = [0, 0]
rare = 0 #If rare = 3, the food becomes "rare" with extra weight (Lab 9)
def peri_new_pos():
    global peri_pos, food_pos, rare
    peri_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    rare = random.randint(0, 3)
peri_new_pos()
peri_spawn = True

# Adding a tick/timer (Lab 9)
tick = 0
 
game_score = 0
 
isRunning = True

def next_level(): #Function that changes the level to next
    global GREEN  #colour change to show progression (Lab 8)
    global level, speed
    GREEN = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    level += 1
    speed += 5  #change in speed for each level (Lab 8)
    
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()  # Fixed sys.quit() to sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            if event.key == pygame.K_4:    #Dev key (Lab 8)
                game_score += 4    
 
    # Move snake based on direction
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10
 
 
    # Insert new position
    snake_body.insert(0, list(snake_pos))  
   
    # Check if food is eaten
    if snake_pos == food_pos:
        food_spawn = False
        game_score += 1
        if game_score % 5 == 0:  #Every 5 foods level changes (Lab 8)
            next_level()  
    else:
        snake_body.pop()

    # mmmmm, perishables (Lab 9)
    if snake_pos == peri_pos:
        peri_spawn = False
        tick = 0
        if rare == 3:
            game_score += 5
            next_level()
        else: 
            game_score += 1
            if game_score % 5 == 0:
                next_level()
    else:
        snake_body.pop
 
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True
        if food_pos == snake_pos or food_pos == block or food_pos == peri_pos: #Check if it's on a snake (Lab 8)
            food_spawn = False     #If it is, reroll (Lab 8)
    
    if not peri_spawn: #Spawning the perishable like normal food (Lab 9)
        peri_new_pos()
        peri_spawn = True
        if peri_pos == snake_pos or peri_pos == block or food_pos == peri_pos: 
            peri_spawn = False 
 
    # Check for collision with walls
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False
 
    # Check for collision with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False
   
   
    # Update screen
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # Perishable changing colour (Lab 9)
    if rare == 3:
        if tick % 20 == 0:
            pygame.draw.rect(screen, D_PURPLISH, pygame.Rect(peri_pos[0], peri_pos[1], 10, 10))
        else:
            pygame.draw.rect(screen, PURPLISH, pygame.Rect(peri_pos[0], peri_pos[1], 10, 10))
    else:
        if tick % 20 == 0:
            pygame.draw.rect(screen, D_PINK, pygame.Rect(peri_pos[0], peri_pos[1], 10, 10))
        else:
            pygame.draw.rect(screen, PINK, pygame.Rect(peri_pos[0], peri_pos[1], 10, 10))
 
    game_score_text = font.render(f"Your score: {game_score}",True,'white')
    level_text = font.render(f"Level {level}",True,'white')   
    screen.blit(game_score_text,(20,20))
    screen.blit(level_text,(500,20))    #Level is now shown (Lab 8)
    pygame.display.update()
 
    pygame.display.flip()
    clock.tick(speed)

    # Adding tick for perishables (Lab 9)
    tick += 1
    if tick == 61:
        tick = 0
        peri_new_pos()


 
game_over_text = font.render("GAME OVER", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text,game_over_rectangle)
pygame.display.update()
pygame.time.wait(100)

pygame.quit()