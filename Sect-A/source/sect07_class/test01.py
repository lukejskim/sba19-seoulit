# 클래스 정의
class BookReader:  # 클래스 BookReader 선언
    #name = str()

    def __init__(self, name, title='서유기'):  # 초기화 함수 재정의
        self.name = name
        self.title = title

    def read_book(self):  # 함수 선언
        print(self.name + '가 ' + self.title + '을 읽습니다.')


# 클래스 호출
reader = BookReader('준영이', '삼국지')     # 인스턴스 생성
reader.read_book()        # 메소드 호출

reader2 = BookReader('찬영이', '초한지')     # 인스턴스 생성
reader2.read_book()        # 메소드 호출

reader3 = BookReader('채영이')     # 인스턴스 생성
reader3.read_book()        # 메소드 호출
