import turtle
t = turtle.Pen()
# 第一个参数线条的颜色，第二个参数需要填充的颜色
t.color('red','yellow')
t.begin_fill()
for i in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
t.hideturtle()
turtle.done()