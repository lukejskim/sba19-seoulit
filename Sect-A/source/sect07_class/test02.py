# 클래스 변수
class People:
    __country = '한국'
    gender = '남자'


print(dir(People))

person = People()

person.__country = '과테말라'
person.gender = '여자'

print('국적 : ', person.__country)
print('성별 : ', person.gender)
