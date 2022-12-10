import turtle
def draw_circle(turtle,color,size,x,y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
square=turtle.Turtle()
square.speed(500)
draw_circle(square, "green", 50, 25, 0)