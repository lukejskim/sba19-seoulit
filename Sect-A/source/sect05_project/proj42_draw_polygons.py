import turtle

side_cnt = int(input("변의 갯수를 입력하세요.[3-8] "))
side_len = int(input("한변의 길이를 입력하세요. [100-300]"))

# side_cnt = 3
# side_len = 150
# angle = 60

turtle.color('red')
turtle.pensize(10)

for i in range (side_cnt):
    angle = 360/side_cnt

    for j in range(side_cnt):
        turtle.forward(side_len)
        turtle.left(angle)

    # 패턴찾기
    turtle.forward(side_len)
    turtle.right(angle)

turtle.done()
