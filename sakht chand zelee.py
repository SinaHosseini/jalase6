import turtle

turtle.bgcolor('grey')
p = turtle.Pen()

big_size = 10
big_size2 = 5
i = 3

p.left(150)
while i <= 10:
    h = (((i - 2) * 180) / i) - 180
    p.pencolor('red')
    for j in range(i):
        p.forward(40 + big_size)
        p.right(h)
    p.pencolor('grey')
    p.right(105)
    p.forward(12.5 + big_size2)
    p.left(105)
    big_size += 15
    big_size2 += 5
    i += 1


turtle.done()
