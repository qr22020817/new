import turtle
# 当前屏幕的尺寸设置
# 国旗分六种尺寸 1号 2880*1920 2号 2400*1600 3号 1920*1280 4号 1440*960 5号 960*640 6号 660*640
turtle.setup(960, 640, 200, 200)
turtle.bgcolor('red')
t = turtle.Pen()
# 确定我们最下边小星星的位置
t.down()
t.color('red')
t.goto(-200,40)
t.up()
t.color('yellow', 'yellow')
# 第一个小星星
t.down()
t.begin_fill()
t.right(30)
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()
t.up()
#第二个星星
t.left(90)
t.right(90)
t.goto(-198,250)
t.down()
t.begin_fill()
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()
t.up()
# 第三个星星
t.left(30)
t.goto(-150,90)
t.down()
t.begin_fill()
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()
t.up()
# 第四个星星
t.left(30)
t.goto(-150,160)
t.down()
t.begin_fill()
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()
t.up()
# 第五个大星星
t.right(30)
t.goto(-400,160)
t.down()
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
t.up()


t.hideturtle()
turtle.done()
