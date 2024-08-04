import pygame
import random

# Initialize Pygame
pygame.init()

# box constraints for the game
WIDTH = 600
HEIGHT = 600

BALL1_RADIUS = 10
BALL2_RADIUS = 10

BALL1_SPEED = [5, 5]
BALL2_SPEED = [5, 5]

BLOCK_SIZE = 50
NUM_BLOCKS_X = WIDTH // BLOCK_SIZE
NUM_BLOCKS_Y = HEIGHT // BLOCK_SIZE

# Colors
# Each ball will the opisite color of its block, and the blocks it hits will change to its color

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BALL1_COLOR = (0, 0, 0)
BALL2_COLOR = (255, 255, 255)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Ying Yang")

# Ball positoining setup
# both balls will be centered vertically, but will be a quarter away from the edges horizontally

ball1_pos = [WIDTH // 4, HEIGHT // 2]
ball1_speed = BALL1_SPEED

ball2_pos = [3 * WIDTH // 4, HEIGHT // 2]
ball2_speed = BALL2_SPEED

# block setup
# to start, hald the blocks will be black and the other half white

# drawing the white blocks, top half of the screen

blocks = []

for i in range(NUM_BLOCKS_X):
    for j in range(NUM_BLOCKS_Y // 2):
        if (i + j) % 2 == 0:
            block = pygame.draw.rect(
                screen, WHITE, (i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )
            blocks.append(block)

# drawing the black blocks, bottom half of the screen
for i in range(NUM_BLOCKS_X):
    for j in range(NUM_BLOCKS_Y // 2, NUM_BLOCKS_Y):
        if (i + j) % 2 == 0:
            block = pygame.draw.rect(
                screen, BLACK, (i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )
            blocks.append(block)


# drawing the balls
def draw_balls():
    pygame.draw.circle(screen, BALL1_COLOR, ball1_pos, BALL1_RADIUS)
    pygame.draw.circle(screen, BALL2_COLOR, ball2_pos, BALL2_RADIUS)


# drawing the blocks
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block.color, block)


# updating the balls postions
def move_balls():
    global ball1_speed, ball2_speed

    ball1_pos[0] += ball1_speed[0]
    ball1_pos[1] += ball1_speed[1]

    ball2_pos[0] += ball2_speed[0]
    ball2_pos[1] += ball2_speed[1]

    # collisioins with window boundaries, and if the radius of the ball itself it out of bounds

    # ball1
    if ball1_pos[0] >= WIDTH - BALL1_RADIUS or ball1_pos[0] <= BALL1_RADIUS:
        ball1_speed[0] = -ball1_speed[0]
    if ball1_pos[1] >= HEIGHT - BALL1_RADIUS or ball1_pos[1] <= BALL1_RADIUS:
        ball1_speed[1] = -ball1_speed[1]

    # ball2
    if ball2_pos[0] >= WIDTH - BALL2_RADIUS or ball2_pos[0] <= BALL2_RADIUS:
        ball2_speed[0] = -ball2_speed[0]
    if ball2_pos[1] >= HEIGHT - BALL2_RADIUS or ball2_pos[1] <= BALL2_RADIUS:
        ball2_speed[1] = -ball2_speed[1]
