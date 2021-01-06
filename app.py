"""
Dodger
"""

import sys
import random
import pygame
from pygame.locals import *
from time import gmtime,strftime


IMAGE_PATH = 'static/images/'
SOUND_PATH = 'static/sounds/'

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
FPS = 90

BADDIE_MIN_SIZE = 20
BADDIE_MED_SIZE = 22
BADDIE_MAX_SIZE = 25

BADDIE_MIN_SPEED = 2
BADDIE_MAX_SPEED = 3
ADD_NEW_BADDIE_RATE = 1
PLAYER_MOVE_RATE = 3


def terminate():
    pygame.quit()
    sys.exit()


def wait_for_player_to_press_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return



def player_has_hit_baddie(player_rect, baddies):
    for b in baddies:
        if player_rect.colliderect(b['rect']):
            return True
    return False

def player_has_hit_object(player_rect,baddies,surface):
    for b in baddies:
        if player_rect.colliderect(b['rect']):
            return surface.blit(player_image,b['rect'])



def draw_text(text, font, surface, x, y):
    text_obj = font.render(text, 1, TEXT_COLOR)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)



pygame.init()
main_clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dodger Game')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 35)

# sounds
game_over_sound = pygame.mixer.Sound(SOUND_PATH + 'game_over.wav')
pygame.mixer.music.load(SOUND_PATH + 'house_lo.mp3')

# images
p_image = pygame.image.load(IMAGE_PATH + 'player.png')
power_1 = pygame.image.load(IMAGE_PATH +'1.png')
power_1_2 = pygame.image.load(IMAGE_PATH + '2.png')
power_1_3 = pygame.image.load(IMAGE_PATH + '3.png')

power_5 = pygame.image.load(IMAGE_PATH + 'green.png')

power_2 = pygame.image.load(IMAGE_PATH +'fire.png')

power_3_1 = pygame.image.load(IMAGE_PATH +'1.png')
power_3_2 = pygame.image.load(IMAGE_PATH + '2.png')
power_3_3 = pygame.image.load(IMAGE_PATH + '3.png')

power_4 = pygame.image.load(IMAGE_PATH + 'snowflake.png')


power_1_image = pygame.transform.scale(power_1,(20,20))
power_1_2_image = pygame.transform.scale(power_1_2,(20,20))
power_1_3_image = pygame.transform.scale(power_1_3,(20,20))
power_4_image = pygame.transform.scale(power_4,(20,20))

power_5_image = pygame.transform.scale(power_5,(10,10))

power_2_image = pygame.transform.scale(power_2,(20,20))
player_image = pygame.transform.scale(p_image, (40, 40))


power_1_rect = power_1_image.get_rect()
power_1_2_rect = power_1_2_image.get_rect()
power_1_3_rect = power_1_3_image.get_rect()

power_4_rect = power_4_image.get_rect()
power_2_rect = power_2_image.get_rect()
player_rect = player_image.get_rect()

power_5_rect = player_image.get_rect()

power_1_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))
power_1_2_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))
power_1_3_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))
power_4_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))

power_5_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))

power_2_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))

baddie_image = pygame.image.load(IMAGE_PATH + 'baddie.png')

# display the start screen
window_surface.fill(BACKGROUND_COLOR)
draw_text('Dodger', font, window_surface, (WINDOW_WIDTH/3), (WINDOW_HEIGHT/3))
draw_text('Press any key to start the game', font, window_surface, (WINDOW_WIDTH/5) - 30, (WINDOW_HEIGHT/3) + 50)
pygame.display.update()
wait_for_player_to_press_key()

top_score = 0
level = 1
levelup_score = 200
now = ''
seconds = ''
seconds_2 = ''
time_power = 0
time_power_2 = 0
strong = ''
i = 1

seconds_3 = ''

seconds_4 = ''


while True:
    # Setting up the start of the game
    baddies = []
    baddies_left = []
    baddies_right = []
    score = 0
    player_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT-50)
    move_left = move_right = move_up = move_down = False
    reverse_cheat = slow_cheat = freze = vulner = kill = False
    baddie_add_counter = 0
    pygame.mixer.music.play(-1, 0.0)
    
    PLAYER_MOVE_RATE = 3
    seconds_2 = ''

    #slow cheat
    slow_cheat = False
    seconds = ''
    
    # the game loop runs while the game is running
    while True:

        
        now = strftime('%M%S',gmtime())

        if seconds_4 != '':
            if int(seconds_4) < int(now):
                for b in baddies_left:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                for b in baddies_right:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                for b in baddies:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                freze = False
                seconds_4 = ''
        
        if seconds_3 != '':
            if int(seconds_3) > int(now):
                strong = -1 * (int(now) - int(seconds_3))
            elif int(seconds_3) == int(now):
                strong = 0
            elif int(seconds_3) < int(now):
                strong = ''
                
        if seconds_4 != '':
            if int(seconds_4) < int(now):
                for b in baddies_left:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                for b in baddies_right:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                for b in baddies:
                    b['speed'] = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)
                freze = False
                seconds_4 = ''
            
        score += 1

        if levelup_score == score:
            levelup_score  = levelup_score + 300
            level += 1
            draw_text(f'Level : {level}', font, window_surface, 10, 80)
            draw_text(f'Next Level: {levelup_score}',font,window_surface,10,120)
            
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverse_cheat = True
                if event.key == K_x:
                    slow_cheat = True
                if event.key == K_LEFT or event.key == K_a:
                    move_right = False
                    move_left = True
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = True
                    move_left = False
                if event.key == K_UP or event.key == K_w:
                    move_down = False
                    move_up = True
                if event.key == K_DOWN or event.key == K_s:
                    move_down = True
                    move_up = False
            if event.type == KEYUP:
                if event.key == K_z:
                    reverse_cheat = False
                if event.key == K_x:
                    slow_cheat = False
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False

            if event.type == MOUSEBUTTONUP:
                # if the mouse moves, move the player to the mouse pointer
                player_rect.centerx = event.pos[0]
                player_rect.centery = event.pos[1]

        # if necessary, add new humans
        if not reverse_cheat and not slow_cheat and not freze:
            if score < 1000:
                baddie_add_counter += round(random.randint(0,7)/10)
                ADD_NEW_BADDIE_RATE = 3
        
            elif score < 10000:
                baddie_add_counter += round(random.randint(0,8)/10)
                ADD_NEW_BADDIE_RATE = 4
                
            elif score < 100000:
                baddie_add_counter += round(random.randint(0,10)/10)
                ADD_NEW_BADDIE_RATE = 5
                
        if baddie_add_counter >= ADD_NEW_BADDIE_RATE:
            baddie_add_counter = 0
            baddie_size = random.choice([BADDIE_MIN_SIZE, BADDIE_MED_SIZE , BADDIE_MAX_SIZE])

            #if the level is less than 2 relese from top
            if level < 3:
                new_baddie = {
                    'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - baddie_size),
                                    0 - baddie_size, baddie_size, baddie_size),
                'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                    }
                baddies.append(new_baddie)

            #if the level is less than 3 release from top,left randomly
            elif level < 5:
                i = random.randint(0,2)
                if i == 1:
                    new_baddie_1 = {
                        'rect': pygame.Rect(0 - baddie_size,random.randint(0, WINDOW_WIDTH - baddie_size)
                                            , baddie_size, baddie_size),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                        }
                    baddies_left.append(new_baddie_1)
                elif i == 0:
                    new_baddie = {
                        'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - baddie_size),
                                            0 - baddie_size, baddie_size, baddie_size),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                        }
                    baddies.append(new_baddie)
                    
            #if the level is higher than 2 release from top,left,right randomly
            elif level > 4:
                i = random.randint(0,3)
                if i == 0:
                    new_baddie = {
                        'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - baddie_size),
                                            0 - baddie_size, baddie_size, baddie_size),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                        }
                    baddies.append(new_baddie)
                elif i == 1:
                    new_baddie_1 = {
                        'rect': pygame.Rect(0 - baddie_size,random.randint(0, WINDOW_HEIGHT - baddie_size)
                                            , baddie_size, baddie_size),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                        }
                    baddies_left.append(new_baddie_1)
                elif i == 2:
                    new_baddie_2 = {
                        'rect': pygame.Rect(WINDOW_WIDTH + baddie_size,random.randint(0, WINDOW_HEIGHT-baddie_size), baddie_size, baddie_size),
                        'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                        'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))
                        }
                    baddies_right.append(new_baddie_2)

        
        
        # player movement
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * PLAYER_MOVE_RATE, 0)
        if move_right and player_rect.right < WINDOW_WIDTH:
            player_rect.move_ip(PLAYER_MOVE_RATE, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * PLAYER_MOVE_RATE)
        if move_down and player_rect.bottom < WINDOW_HEIGHT:
            player_rect.move_ip(0, PLAYER_MOVE_RATE)

        # move the humans down
        for b in baddies:
            if not reverse_cheat and not slow_cheat and not freze:
                b['rect'].move_ip(0, b['speed'])
            elif freze:
                b['rect'].move_ip(0,0)
            elif reverse_cheat:
                b['rect'].move_ip(0, -5)
            elif slow_cheat:
                b['rect'].move_ip(0, 1)

        for b in baddies_left:
            if not reverse_cheat and not slow_cheat and not freze:
                b['rect'].move_ip(b['speed'],0)
            elif freze:
                b['rect'].move_ip(0,0)
            elif reverse_cheat:
                b['rect'].move_ip(-5, 0)
            elif slow_cheat:
                b['rect'].move_ip(1, 0)

        for b in baddies_right:
            if not reverse_cheat and not slow_cheat and not freze:
                b['rect'].move_ip(-1 * b['speed'],0)
            elif freze:
                b['rect'].move_ip(0,0)
            elif reverse_cheat:
                b['rect'].move_ip(5,0)
            elif slow_cheat:
                b['rect'].move_ip(-1,0)
                

        # remove the humans who fell behind the bottom of the screen
        for b in baddies[:]:
            if b['rect'].top > WINDOW_HEIGHT:
                baddies.remove(b)
            if kill:
                baddies.remove(b)

        for b in baddies_left[:]:
            if b['rect'].left > WINDOW_WIDTH:
                baddies_left.remove(b)
            if kill:
                baddies_left.remove(b)

        for b in baddies_right[:]:
            if b['rect'].left < 0:
                baddies_right.remove(b)
            if kill:
                baddies_right.remove(b)
                
        kill = False

        # display the game world in the window
        window_surface.fill(BACKGROUND_COLOR)

        # display the number of points and the best result
        draw_text(f'Score: {score}', font, window_surface, 10, 0)
        draw_text(f'Best score: {top_score}', font, window_surface, 10, 40)
        draw_text(f'Level : {level}', font, window_surface, 10, 80)
        draw_text(f'Next Level: {levelup_score}',font,window_surface,10,120)
        
        if seconds_3 != '':
            draw_text(f'strong : {strong}s',font,window_surface,10,160)
        else:
            if seconds_3 == '' :
                draw_text('strong : 0s ',font,window_surface,10,160)
                

        # display player
        window_surface.blit(player_image, player_rect)

        # display powers
        window_surface.blit(power_1_image,power_1_rect)
        window_surface.blit(power_1_2_image,power_1_2_rect)
        window_surface.blit(power_1_3_image,power_1_3_rect)

        window_surface.blit(power_4_image,power_4_rect)
        
        window_surface.blit(power_2_image,power_2_rect)

        window_surface.blit(power_5_image,power_5_rect)

        # display every human
        for b in baddies:
            window_surface.blit(b['surface'], b['rect'])

        for b in baddies_left:
            window_surface.blit(b['surface'],b['rect'])

        for b in baddies_right:
            window_surface.blit(b['surface'],b['rect'])

        pygame.display.update()

        # check if any of the humans hit the player
        if player_has_hit_baddie(player_rect,baddies_left):
            if vulner == True:
                player_has_hit_object(player_rect,baddies_left,window_surface)
                continue
            if score > top_score:
                top_score = score
            level = 1
            levelup_score = 200
            break

        if player_has_hit_baddie(player_rect,baddies):
            if vulner == True:
                player_has_hit_object(player_rect,baddies,window_surface)
                continue
            if score > top_score:
                top_score = score
            level = 1
            levelup_score = 200
            break
        
        if player_has_hit_baddie(player_rect,baddies_right):
            if vulner == True:
                player_has_hit_object(player_rect,baddies_right,window_surface)
                continue
            if score > top_score:
                top_score = score
            level = 1
            levelup_score = 200
            break

        
        #checks if power is done
        if seconds != '':
            if int(now)  >= (int(seconds)):
                slow_cheat = False
                time_power = 0
                seconds = ''
    
        if seconds_2 != '':
            if int(now) >= (int(seconds_2) + time_power_2):
                PLAYER_MOVE_RATE = 3
                time_power_2 = 0
                seconds_2 = ''
                
        if seconds_3 != '':
            if int(now) >= (int(seconds_3)):
                time_power_3 = 0
                seconds_3 = ''
                vulner = False
                
        #checks if power hit player to apply powers
        if Rect.colliderect(player_rect,power_1_rect):
            power_1_rect.topleft = (random.randint(0,600),random.randint(0,600))
            if random.randint(0,11) > 5:
                vulner = True
                seconds_3 = str(int(strftime('%M%S',gmtime())) + 1)
            else:
                slow_cheat = True
            seconds = str(int(strftime('%M%S',gmtime())) + 1)

        if Rect.colliderect(player_rect,power_1_2_rect):
            power_1_2_rect.topleft = (random.randint(0,600),random.randint(0,600))
            if random.randint(0,11) > 5:
                vulner = True
                seconds_3 = str(int(strftime('%M%S',gmtime())) + 3)
                
            else:
                slow_cheat = True
                seconds = str(int(strftime('%M%S',gmtime())) + 3)

        if Rect.colliderect(player_rect,power_1_3_rect):
            power_1_3_rect.topleft = (random.randint(0,600),random.randint(0,600))
            if random.randint(0,11) > 5:
                vulner = True
                seconds_3 = str(int(strftime('%M%S',gmtime()))+5)
            else:
                slow_cheat = True
            seconds = str(int(strftime('%M%S',gmtime())) + 5)

        if Rect.colliderect(player_rect,power_2_rect):
            power_2_rect.topleft = (random.randint(0,600),random.randint(0,600))
            PLAYER_MOVE_RATE = 5
            seconds_2 =  str(int(strftime('%M%S',gmtime())) + random.choice([1,3,5]))

        if Rect.colliderect(player_rect,power_4_rect) and not slow_cheat:
            power_4_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))
            seconds_4 = str(int(strftime('%M%S',gmtime())) + random.choice([2,3,5]))
            freze = True
            for b in baddies_left:
                b['speed'] = 0
            for b in baddies_right:
                b['speed'] = 0
            for b in baddies:
                b['speed'] = 0

        if Rect.colliderect(player_rect,power_5_rect):
            power_5_rect.topleft = (random.randint(0,WINDOW_WIDTH-40),random.randint(0,WINDOW_HEIGHT-40))
            kill = True
        
        
            
        main_clock.tick(FPS)

    # displaying the game and displaying the caption 'Game over'
    pygame.mixer.music.stop()
    game_over_sound.play()

    draw_text('GAME OVER!', font, window_surface, (WINDOW_WIDTH/3), (WINDOW_HEIGHT/3))
    draw_text('Press any key to start new game', font, window_surface,
              (WINDOW_WIDTH/3) - 120, (WINDOW_HEIGHT / 3) + 50)

    pygame.display.update()
    wait_for_player_to_press_key()

    game_over_sound.stop()
