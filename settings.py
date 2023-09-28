# Game options/settings
TITLE = "Snake"
GRID_SIZE = 30
BLANK_SIZE = 40
ROWS = 10
COLS = 10
FPS = 80
FONT_NAME = 'arial'


# Define colors
WHITE = (255, 255, 255)
WHITE1 = (220, 220, 220)
WHITE2 = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = BLACK
LINE_COLOR = BLUE1

INF = 100000000

# AI settings
N_INPUT = 32
N_HIDDEN1 = 20
N_HIDDEN2 = 12
N_OUTPUT = 4
GENES_LEN = N_INPUT * N_HIDDEN1 + N_HIDDEN1 * N_HIDDEN2 + N_HIDDEN2 * N_OUTPUT + N_HIDDEN1 + N_HIDDEN2 + N_OUTPUT 
P_SIZE = 100
C_SIZE = 400
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MUTATE_RATE = 0.1

# path
# store_parent_path = "./tmp/"
store_parent_path = "./tmp/v2/"

def makeDirsExist():
    import os
    dirs = [
        f"{store_parent_path}genes",
        f"{store_parent_path}genes/all",
        f"{store_parent_path}genes/best",
        f"{store_parent_path}seed",
    ]

    for dir in dirs:
        print(f"dir {dir}")
        if not os.path.exists(dir):
            os.makedirs(dir)

makeDirsExist()
