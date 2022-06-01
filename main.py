import pygame
import cv2 as cv
from character import Character

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

# Create character
character = Character()


# create webcam
webcam = cv.VideoCapture(0)


# # read returns 2 things (tuple)
# # 1) if reading the frame was successful
# # 2) the frame that is being read from the webcam
# successful_frame_read, frame = webcam.read()
#
# # Must convert to grayscale
# gray_scaled_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
# # Detect faces
# # whatever this classifier is then we want to detect all the faces with multiscale (size doesn't matter)
# # this is based off whatever you chose to detect, and we chose faces
# # this returns a tuple with the otp left coordinate and the width and height (x, y, w, h)
# face_coordinates = trained_face_data.detectMultiScale(gray_scaled_frame)
# print(face_coordinates)

# this is here in case face is not detected right away
x = 0

running = True
while running:

    # Set background
    screen.blit(background, (-200, 0))


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
                x, y, w, h = face_coordinates[0]

    except IndexError:
        print("return to screen")

    screen.blit(character.image, ((x + 100) * 1.1, 600))

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()