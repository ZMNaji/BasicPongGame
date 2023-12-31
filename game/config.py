# Game config
SCREEN_W = 1280
SCREEN_H = 720
MAIN_BG = "black"
FPS = 60


# Paddle config
PADDLE_SIZE = (SCREEN_W / 64, SCREEN_H / 8)
LEFT_PADDLE_POSITION = (PADDLE_SIZE[0], SCREEN_H / 2)
RIGHT_PADDLE_POSITION = (SCREEN_W - PADDLE_SIZE[0] * 2, SCREEN_H / 2)
PADDLE_SPEED = 5


# Ball config
BALL_POSITION = (SCREEN_W / 2, SCREEN_H / 2)
BALL_RAD = 10
BALL_SPEED = (5, 5)


# Ball config
ABILITY_SPEED = 2


# Music Config
MUSIC_VOLUME = 0.1


# Clock Config
CLOCK_TEXT_COLOR = (255, 255, 255)
CLOCK_TEXT_SIZE = 20


# Clock Config
SCORE_TEXT_COLOR = (255, 255, 255)
SCORE_TEXT_SIZE = 20
