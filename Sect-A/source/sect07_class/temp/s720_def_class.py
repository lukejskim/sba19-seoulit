# 클래스 정의
class BookReader:        # 클래스 BookReader 선언
    name = str()            # 문자열형 변수 name 선언

    def read_book():
        print(name + ' is reading Book!!')


reader = BookReader()
print(type(reader))

reader.name = 'Twise'
reader.read_book()