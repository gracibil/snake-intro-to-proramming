from ipy_lib3 import SnakeUserInterface
from Coordinate_Row_Class import CoordinateRow
from Coordinate_Class import Coordinate

WIDTH = 32
HEIGHT = 24
EMPTY = 0
APPLE = 1
SNAKE = 2
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'


def check_crash():
    global game_state
    current_coord = snake.get_last_coord()
    for i in snake.coordniate_row[:-1]:
        if i == current_coord:
            print('Game over, you crashed')
            game_state = False


def place_apple():
    global apple
    global apple_coords
    apple_coords = (ui.random(WIDTH), ui.random(HEIGHT))
    ui.place(apple_coords[0], apple_coords[1], APPLE)
    ui.show()
    apple = True


def remove_piece():
    first_coord = snake.remove_coordinate()
    ui.place(first_coord[0], first_coord[1], EMPTY)


def move_snake():
    last_coord = snake.get_last_coord()
    ui.place(last_coord[0], last_coord[1], 2)
    ui.show()
    coord = Coordinate(last_coord[0], last_coord[1])
    return coord


def process_animation(event, direction):
    global apple_coords
    global apple

    if direction == LEFT:
        coord = move_snake()
        snake.add_coordinate(coord.sub_coord_x())
        for i in snake.coordniate_row:
            if i == apple_coords:
                apple = False
                ui.place(apple_coords[0], apple_coords[1], SNAKE)
                snake.add_coordinate(coord.sub_coord_x())
        remove_piece()

    if direction == RIGHT:
        coord = move_snake()
        snake.add_coordinate(coord.add_coord_x())
        for i in snake.coordniate_row:
            if i == apple_coords:
                apple = False
                ui.place(apple_coords[0], apple_coords[1], SNAKE)
                snake.add_coordinate(coord.add_coord_x())
        remove_piece()

    if direction == UP:
        coord = move_snake()
        snake.add_coordinate(coord.sub_coord_y())
        for i in snake.coordniate_row:
            if i == apple_coords:
                apple = False
                ui.place(apple_coords[0], apple_coords[1], SNAKE)
                snake.add_coordinate(coord.sub_coord_y())
        remove_piece()

    if direction == DOWN:
        coord = move_snake()
        snake.add_coordinate(coord.add_coord_y())
        for i in snake.coordniate_row:
            if i == apple_coords:
                apple = False
                ui.place(apple_coords[0], apple_coords[1], SNAKE)
                snake.add_coordinate(coord.add_coord_y())
        remove_piece()


def process_direction(event):
    global direction
    if event.data == LEFT:
        if direction != RIGHT:
            direction = LEFT
    if event.data == RIGHT:
        if direction != LEFT:
            direction = RIGHT
    if event.data == UP:
        if direction != DOWN:
            direction = UP
    if event.data == DOWN:
        if direction != UP:
            direction = DOWN


'----------program start-----------'

ui = SnakeUserInterface(WIDTH, HEIGHT)
ui.set_animation_speed(15)
ui.show()

Coordinate.width = WIDTH
Coordinate.height = HEIGHT

direction = RIGHT
snake = CoordinateRow()
game_state = True
apple = False
apple_coords = ()
move_snake()

while game_state:
    event = ui.get_event()

    if event.name == 'alarm':
        process_animation(event, direction)
    if event.name == 'arrow':
        process_direction(event)
    if not apple:
        place_apple()
    check_crash()
