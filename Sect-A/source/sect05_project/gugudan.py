#준영이가 스스로 만든 구구단_01
단 = int(input('구구단을 몇단을 출력 할까요? 숫자를 입력하세요.:     '))
print(단, '단')
for x in  range(1, 10):
    값 = int(단 * x )
    print(단, ' x ', x, ' = ', 값)

