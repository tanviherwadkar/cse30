import turtle
cturtle = turtle.Turtle()

def set_canvas(t, color='ivory', length=200, width=400, title='Digital Art'):
  t.color('burlywood')
  t.screen.bgcolor('bisque')
  t.pensize(5)
  t.hideturtle()
  t.pendown()

def flip(arr):
  for i, el in enumerate(arr):
    if el == "R":
      arr[i] = "L"
    elif el == "L":
      arr[i] = "R"
  return arr

def turns(depth):

  R = "R"
  L = "L"

  if depth == 0:
    return []
  
  elif depth == 1:
    return [L]
  
  else:
    dup = turns(depth-1)
    dup_rev = dup[::-1]
    return dup + [L] + flip(dup_rev)

def create_dragon(t, depth, size=5):
  set_canvas(t=cturtle)
  directions = turns(depth)
  for i in directions:
    if i == "R":
      t.right(90)
      t.forward(size)
    elif i == "L":
      t.left(90)
      t.forward(size)

create_dragon(cturtle, 9, 7)