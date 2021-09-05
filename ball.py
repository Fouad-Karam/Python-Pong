from turtle import Turtle

SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = SPEED
        self.y_move = SPEED
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Detect collision with top and bottom walls only
    def y_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    # Detect collision with paddles only
    def x_r_bounce(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def x_l_bounce(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.x_r_bounce()
        self.x_l_bounce()
