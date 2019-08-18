import turtle as t

t.pensize(3)

# 삼각형 만들기
t.penup()
t.goto(-200, -50)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(40, steps=3)
t.end_fill()

# 사각형 만들기
t.penup()
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(40, steps=4)
t.end_fill()

# 오각형 만들기
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color('green')
t.circle(40, steps=5)
t.end_fill()

# 육각형 만들기
t.penup()
t.goto(100, -50)
t.pendown()
t.begin_fill()
t.color('yellow')
t.circle(40, steps=6)
t.end_fill()

# 원 만들기
t.penup()
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color('purple')
t.circle(40)
t.end_fill()

t.color('green')
t.penup()
t.goto(-100, 50)
t.pendown()
t.write("도형 색칠하기")

t.done()
