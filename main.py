import pygame
import cv2 as cv
from character import Character
from ball import Ball
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# initialize pygame
pygame.init()

trained_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# create screen
pygame.display.set_caption("Soccer Header")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load Background
background = pygame.image.load('images/background.jpeg')
# background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# functions

def is_collision(ball_x, ball_y, character_x, character_y):

    # distance = math.sqrt(math.pow(ball_x - character_x, 2) + math.pow(ball_y - character_y, 2))
    # if distance < 100:
    #     print("good header")
    #     return True
    # else:
    #     return False

    # half of the balls size
    ball_x += 55
    if ball_x > character_x and ball_x < character_x + 200 and ball_y > 600:
        print("good header")
        return True
    else:
        return False


# score
score_value = 0
font = pygame.font.Font('SoccerScoreboard-XmMg.ttf', 64)


def show_score(x, y):
    # first you have to render text then you can blit it on the screen
    score = font.render("Score: " + str(score_value), True, (0, 175, 0))
    screen.blit(score, (x, y))


# Create character
character = Character()

# balls = []
#
# for i in range(3):
#     balls.append(Ball())

ball1 = Ball()
ball2 = Ball()
ball3 = Ball()

# create webcam
webcam = cv.VideoCapture(0)


# this is here in case face is not detected right away
character_x = 0


running = True
while running:

    # Set background
    screen.blit(background, (-200, 0))
    show_score(10, 10)

    # TODO: can't figure out how to use a for loop for balls, balls will not respawn
    # for ball in balls:
    #     x, y = ball.get_x_y_coord()
    #     if ball.is_active:
    #         screen.blit(ball.get_img(), (x, y))
    #         ball.drop_ball()
    #     else:
    #         ball = Ball()

    # TODO: had to hard code each ball
    if ball1.is_active:
        if is_collision(ball1.x_pos, ball1.y_pos, character_x, 600):
            ball1 = Ball()
            score_value += 1
        screen.blit(ball1.get_img(), (ball1.x_pos, ball1.y_pos))
        ball1.drop_ball()
    else:
        ball1 = Ball()

    if ball2.is_active:
        if is_collision(ball2.x_pos, ball2.y_pos, character_x, 600):
            ball2 = Ball()
            score_value += 1
        screen.blit(ball2.get_img(), (ball2.x_pos, ball2.y_pos))
        ball2.drop_ball()
    else:
        ball2 = Ball()

    if ball3.is_active:
        if is_collision(ball3.x_pos, ball3.y_pos, character_x, 600):
            ball3 = Ball()
            score_value += 1
        screen.blit(ball3.get_img(), (ball3.x_pos, ball3.y_pos))
        ball3.drop_ball()
    else:
        ball3 = Ball()

    # finding character coordinates
    successful_frame_read, frame = webcam.read()
    frame = cv.flip(frame, 1)
    # Must convert to grayscale
    gray_scaled_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(gray_scaled_frame, 1.1, minSize=(150, 150))
    # for el in face_coordinates:
    #     x, y, w, h = el

    try:
        if face_coordinates is not None:
            if face_coordinates[0] is not None:
                character_x, y, w, h = face_coordinates[0]

    except IndexError:
        print("return to screen")

    screen.blit(character.image, (character_x * 1.1, 600))

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()