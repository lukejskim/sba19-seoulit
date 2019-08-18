# 클래스 변수와 인스턴스 변수
# 변수의 선언위체 따라 달라지는 유효범위
class BookReader:
    country = 'South Korea'       # 클래스변수 country 선언

    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name          # 인스턴스 변수 name 선언

    def read_book(self):
        print(self.name + ' is reading Book!!')


# 객체 인스턴스화
reader1 = BookReader('Chanyoung')
reader2 = BookReader('Juneyoung')
reader3 = BookReader('Cheyoung')

reader1.country = 'America'
reader2.country = 'China'

# 클래스변수 country 확인
print('reader1.country : ', reader1.country)
print('reader2.country : ', reader2.country)
print('reader3.country : ', reader3.country)

# 클래스함수 호출 (인스턴스 변수 name 출력)
reader1.read_book()
reader2.read_book()
reader3.read_book()
