
class 동물:
    tribe = '동물'
    def __init__(self, name):
        self.name = name

    def 소개(self):
        print('나는', self.tribe,  self.name, '입니다.')

class 육식동물(동물):
    def __init__(self, name):
        self.name = name
        self.tribe = '육식동물'

    def 좋아하는음식(self):
        print('나는 고기를 좋아합니다.')

class 초식동물(동물):
    def __init__(self, name):
        self.name = name
        self.tribe = '초식동물'

    def 좋아하는음식(self):
        print('나는 풀을 좋아합니다.')


print('-' * 50, "\n[육식동물 객체 생성]")
tiger = 육식동물('호랑이')
tiger.소개()
tiger.좋아하는음식()


print('-' * 50, "\n[초식동물 객체 생성]")
rabit = 초식동물('토끼')
rabit.소개()
rabit.좋아하는음식()