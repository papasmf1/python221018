# -*- 생성자와 소멸자 -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
d = MyClass(5)
#명시적으로 소멸
#del d 

print("전체 코드 실행 종료")
