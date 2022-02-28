from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        one_piece = Turtle(shape="square")
        one_piece.color("white")
        one_piece.speed("slowest")
        one_piece.penup()
        one_piece.goto(position)
        self.pieces.append(one_piece)

    def extend(self):
        #     Add a new segment to the snake
        self.add_segment(self.pieces[-1].position())

    def change_color(self, color):
        for one_piece in self.pieces:
            one_piece.color(color)

    def move(self):
        for piece_num in range(len(self.pieces) - 1, 0, -1):
            x = self.pieces[piece_num - 1].xcor()
            y = self.pieces[piece_num - 1].ycor()
            self.pieces[piece_num].goto(x, y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
