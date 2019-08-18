# 클래스 초기화 함수, __init__() 재정의
class BookReader:               # 클래스 BookReader 선언
    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name

    def read_book(self):        # 함수 선언
        print(self.name + ' is reading Book!!')


# 원래대로 인자값 없이 객체를 생성시, 에러가 발생
# reader = BookReader()

# 이름을 넣고 객체 생성
reader = BookReader('Daniel')  # 객체 생성
reader.read_book()             # 메소드 호출

