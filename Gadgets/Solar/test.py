import turtle
turtle.speed(999)
size = float(input('Star Size'))
color = input('Star Color')
turtle.color(color)
if size > 20:
  print('Woah! This might take a while...')
while size > 0:
  turtle.circle(size)
  size -= .15