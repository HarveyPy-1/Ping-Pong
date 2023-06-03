from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def move_left(self):
        if self.x_move > 0:
            self.x_move *= -1
        elif self.y_move > 0:
            self.y_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.move_speed = 0.1
        self.goto(new_x, new_y)

    def move_right(self):
        if self.x_move < 0:
            self.x_move *= -1
        if self.y_move < 0:
            self.y_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.move_speed = 0.1
        self.goto(new_x, new_y)
        
        
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        