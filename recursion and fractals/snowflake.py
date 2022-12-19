import turtle

cturtle = turtle.Turtle()

def set_canvas(t, color='ivory', length=200, width=400, title='Digital Art'):
  t.color('burlywood')
  t.screen.bgcolor('bisque')
  t.hideturtle()
  t.pensize(5)
  t.pendown()
  return t

def curve(t, length, depth):
  if depth == 0:
    t.forward(length)
  else:
    new_l = length / 3
    new_d = depth - 1

    curve(t, new_l, new_d)
    t.right(60)
    curve(t, new_l, new_d)
    t.left(120)
    curve(t, new_l, new_d)
    t.right(60)
    curve(t, new_l, new_d)
#clear()

def snowflake(t, length, depth):
  t = set_canvas(t=cturtle)
  for i in range(3):
    curve(t, length, depth)
    t.left(120)

snowflake(cturtle, 200, 2)