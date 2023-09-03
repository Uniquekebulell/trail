import turtle as t

'''
绘制五星红旗：
1.设置画笔属性：速度，颜色，填充颜色
2.绘制：红色背景画布 + 五角星
'''

t.speed(10)
t.hideturtle()       #隐藏海龟
# t.fillcolor('red')   #海龟填充为红色
# t.pencolor('blue')
t.color('red')

#绘制画布
t.pensize(10)
t.penup()
t.goto(-400,300)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(600)
    t.right(90)
t.end_fill()

#大五角星，五角星的角的度数是36,72,108
t.color('yellow')
t.penup()
t.goto(-310,200)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()

#第1个小五角星
t.color('yellow')
t.penup()
t.goto(-190,250)
t.pendown()
t.right(30)
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

#第2个小五角星
t.color('yellow')
t.penup()
t.goto(-150,200)
t.pendown()
t.left(45)
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

#第3个小五角星
t.color('yellow')
t.penup()
t.goto(-150,140)
t.pendown()
t.right(30)
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

#第4个小五角星
t.color('yellow')
t.penup()
t.goto(-190,100)
t.pendown()
t.right(30)
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

# res = t.Screen()
# print(res.screensize())
t.done()
