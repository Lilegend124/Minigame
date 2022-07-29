#Jiafu Li
#jl8jp

"""
Citations:
naruto(player 2) and tree log sprite: https://spritedatabase.net/file/1008
sasuke sprite(player 1) : https://spritedatabase.net/file/1009
shurikens sprite: https://spritedatabase.net/file/1011
"""


import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# Score
score = 0

# Gravity
gravity = 9.8

# Falling objects
wood = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood1 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood2 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood3 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood4 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood5 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood6 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100), 'wood.png')
wood7 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood8 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood9 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')
wood10 = gamebox.from_image(random.randint(50, 760),random.randint(0, 100),'wood.png')

bonus = gamebox.from_image(random.randint(50, 700),random.randint(0, 100),'bonus.png')
bonus.scale_by(0.3)

# Basic background / ground
ground = gamebox.from_color(0,0, 'dark red', 5000 ,120)
ground.bottom = camera.bottom


# background
background = gamebox.from_image(400,100,'naruto_stage.png')
background.scale_by(2)

# timer
time = 1800

# character
sprite_stand = gamebox.load_sprite_sheet('sasuke_still.png', 1, 4)
sprite_right = gamebox.load_sprite_sheet('sasuke_right.png', 1, 8)
stand_animation = []
right_animation = []

sprite_naruto_stand = gamebox.load_sprite_sheet('naruto_still.png', 1, 4)
sprite_naruto_left = gamebox.load_sprite_sheet('naruto_left.png', 1, 8)
stand_naruto_animation = []
left_naruto_animation = []

for image in sprite_naruto_stand:
    stage = gamebox.from_image(0, 0, image)
    stage.bottom = ground.top
    stage.left = camera.left + 500
    stand_naruto_animation.append(stage)

for image in sprite_naruto_left:
    stage = gamebox.from_image(0, 0, image)
    stage.bottom = ground.top
    stage.left = camera.left + 500
    left_naruto_animation.append(stage)

for image in sprite_stand:
    stage = gamebox.from_image(0, 0, image)
    stage.bottom = ground.top
    stage.left = camera.left + 100
    stand_animation.append(stage)

for image in sprite_right:
    stage = gamebox.from_image(0, 0, image)
    stage.bottom = ground.top
    stage.left = camera.left + 100
    right_animation.append(stage)

def draw_objects():
    """
    Draws the collectables within the game, also repositions them so they keep falling
    :return: None
    """
    wood.y += gravity
    wood1.y += gravity
    wood2.y += gravity
    wood3.y += gravity
    wood4.y += gravity
    wood5.y += gravity
    wood6.y += gravity
    wood7.y += gravity
    wood8.y += gravity
    wood9.y += gravity
    wood10.y += gravity
    bonus.y += gravity

    camera.draw(wood)
    camera.draw(wood1)
    camera.draw(wood2)
    camera.draw(wood3)
    camera.draw(wood4)
    camera.draw(wood5)
    camera.draw(wood6)
    camera.draw(wood7)
    camera.draw(wood8)
    camera.draw(wood9)
    camera.draw(wood10)
    camera.draw(bonus)

    if wood1.y > camera.bottom:
        wood1.y = random.randint(50,100)
    if wood2.y > camera.bottom:
        wood2.y = random.randint(50,100)
    if wood3.y > camera.bottom:
        wood3.y = random.randint(50,100)
    if wood4.y > camera.bottom:
        wood4.y = random.randint(50,100)
    if wood5.y > camera.bottom:
        wood5.y = random.randint(50,100)
    if wood6.y > camera.bottom:
        wood6.y = random.randint(50,100)
    if wood7.y > camera.bottom:
        wood7.y = random.randint(50,100)
    if wood8.y > camera.bottom:
        wood8.y = random.randint(50,100)
    if wood9.y > camera.bottom:
        wood9.y = random.randint(50,100)
    if wood10.y > camera.bottom:
        wood10.y = random.randint(50,100)
    if wood.y > camera.bottom:
        wood.y = random.randint(50,100)

def restart(keys):
    """
    The begining page of the game with instructions, also where the game goes in order to restart
    :param keys: An input from the user by pressing keys
    :return: None
    """
    camera.clear('light blue')
    message8 = gamebox.from_text(75, 50, str("Jiafu Li, jl8jp: Konoha Training Drill"), 50, 'black')
    message = gamebox.from_text(75, 50, str("Press space bar to play"), 36, 'red')
    message2 = gamebox.from_text(75, 20, str("Press a and d to move for player 1"), 36, 'black')
    message4 = gamebox.from_text(0,0, str("Press left and right arrow keys for player 2"), 36, ' black')
    message3 = gamebox.from_text(75,80, str("Increase your score by collecting tree logs"), 36, 'black')
    message5 = gamebox.from_text(0,0,str('Get an even bigger award by catching shurikens! '), 36, 'black')
    message6 = gamebox.from_text(0,0,str('Top left corner is your time, game will end when time is 0'), 36, 'black')
    message7 = gamebox.from_text(0,0, str('Top right corner is your score'), 36, 'black')

    message.x = camera.x                        # Positioning of the messages
    message2.x = camera.x
    message3.x = camera.x
    message4.x = camera.x
    message5.x = camera.x
    message6.x = camera.x
    message7.x = camera.x
    message8.x = camera.x

    message.y = camera.y - 80
    message2.y = camera.y - 50
    message3.y = camera.y + 50
    message4.y = camera.y
    message5.y = camera.y + 80
    message6.y = camera.y + 120
    message7.y = camera.y + 150
    message8.y = camera.y - 180

    messages = [message, message2, message3,message4, message5, message6, message7, message8 ]

    for text in messages:
        camera.draw(text)

    camera.display()
    if pygame.K_SPACE in keys:
        global score
        score = 0
        global time
        time = 1800
        gamebox.timer_loop(30, tick)

def draw_text():
    """
    Draws the different texts shown in game
    :return: None
    """
    global score

    message2 = gamebox.from_text(75, 20, str("Press a and d to move for player 1"), 36, 'black')
    message4 = gamebox.from_text(0, 0, str("Press left and right arrow keys for player 2"), 36, ' black')
    message2.x = camera.x
    message4.x = camera.x
    message4.y = camera.y -250
    message2.y = camera.y - 270

    camera.draw(message2)
    camera.draw(message4)


def tick(keys):
    """
    This is what does most of the drawings, including the two characters shown in game.
    :param keys: An input from the user by pressing keys
    :return: None
    """
    camera.draw(background)
    global score
    global time
    time -= 1
    time_passed = gamebox.from_text(75,50 , 'Time: ' + str(time//30) , 36, 'dark green')
    print(time)
    if time == 1340:
        bonus.y = random.randint(10,100)
        camera.draw(bonus)
    if time == 612:
        bonus.y = random.randint(10,100)
        camera.draw(bonus)

    for stage in stand_animation:                   # Drawing of first character and its interactions with collectables
        stage.move_speed()
        stage.move_to_stop_overlapping(ground)
        if stage.touches(bonus):
            score += 50
            bonus.y = 600
        if stage.touches(wood):
            score += 1
            wood.y = random.randint(50, 100)
        if stage.touches(wood1):
            score += 1
            wood1.y = random.randint(50, 100)
        if stage.touches(wood2):
            score += 1
            wood2.y = random.randint(50, 100)
        if stage.touches(wood3):
            score += 1
            wood3.y = random.randint(50, 100)
        if stage.touches(wood4):
            score += 1
            wood4.y = random.randint(50, 100)
        if stage.touches(wood5):
            score += 1
            wood5.y = random.randint(50, 100)
        if stage.touches(wood6):
            score += 1
            wood6.y = random.randint(50, 100)
        if stage.touches(wood7):
            score += 1
            wood7.y = random.randint(50, 100)
        if stage.touches(wood8):
            score += 1
            wood8.y = random.randint(50, 100)
        if stage.touches(wood9):
            score += 1
            wood9.y = random.randint(50, 100)
        if stage.touches(wood10):
            score += 1
            wood10.y = random.randint(50, 100)

        for right_stage in right_animation:
            if pygame.K_d in keys and stage.bottom_touches(ground):
                right_stage.x += 3
                stage.x = right_stage.x
                camera.draw(right_animation[(time) % len(right_animation)])
            if pygame.K_a in keys and stage.bottom_touches(ground):
                right_stage.x -= 3
                stage.x = right_stage.x
                camera.draw(right_animation[(time) % len(right_animation)])

    for stage in stand_naruto_animation:            # Drawing of second character and its interactions with collectables
        stage.move_speed()
        stage.move_to_stop_overlapping(ground)
        if stage.touches(bonus):
            score += 50
            bonus.y = 600
        if stage.touches(wood):
            score += 1
            wood.y = random.randint(50, 100)
        if stage.touches(wood1):
            score += 1
            wood1.y = random.randint(50, 100)
        if stage.touches(wood2):
            score += 1
            wood2.y = random.randint(50, 100)
        if stage.touches(wood3):
            score += 1
            wood3.y = random.randint(50, 100)
        if stage.touches(wood4):
            score += 1
            wood4.y = random.randint(50, 100)
        if stage.touches(wood5):
            score += 1
            wood5.y = random.randint(50, 100)
        if stage.touches(wood6):
            score += 1
            wood6.y = random.randint(50, 100)
        if stage.touches(wood7):
            score += 1
            wood7.y = random.randint(50, 100)
        if stage.touches(wood8):
            score += 1
            wood8.y = random.randint(50, 100)
        if stage.touches(wood9):
            score += 1
            wood9.y = random.randint(50, 100)
        if stage.touches(wood10):
            score += 1
            wood10.y = random.randint(50, 100)

        for right_stage in left_naruto_animation:
            if pygame.K_RIGHT in keys and stage.bottom_touches(ground):
                right_stage.x += 3
                stage.x = right_stage.x
                camera.draw(left_naruto_animation[(time) % len(left_naruto_animation)])
            if pygame.K_LEFT in keys and stage.bottom_touches(ground):
                right_stage.x -= 3
                stage.x = right_stage.x
                camera.draw(left_naruto_animation[(time) % len(left_naruto_animation)])

    draw_objects()

    if pygame.K_a not in keys and pygame.K_d not in keys:       # Standing animation when nothing is pressed
        camera.draw(stand_animation[(time // 2) % len(stand_animation)])
    if pygame.K_RIGHT not in keys and pygame.K_LEFT not in keys:
        camera.draw(stand_naruto_animation[(time // 2) % len(stand_naruto_animation)])




    current_score = gamebox.from_text(660, 100, 'Score: ' + str(score // 2), 50, 'red')
    camera.draw(current_score)
    camera.draw(time_passed)
    camera.draw(ground)
    draw_text()
    if time == 0:                            # Goes back to first/restart page
        gamebox.pause()
        keys.clear()
        gamebox.timer_loop(30, restart)
    camera.display()

gamebox.timer_loop(30, restart)