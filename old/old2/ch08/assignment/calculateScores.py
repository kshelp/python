# 클래스를 선언합니다.
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    # 인스턴스 함수 
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        Student.count += 1
        Student.students.append(self)
        

    def get_sum(self):
        return self.korean + self.math + self.english

    def get_average(self):
        return self.get_sum() / 3

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())    

while True:
    input_string = input("학생정보입력(그만두기: q) ");
    sl = input_string.split()
    print(sl)

    if(sl[0]=="q"):
        Student.print()
        break
    else:
        #Student("유재석", 87, 98, 88, 95)
        Student(sl[0], int(sl[1]), int(sl[2]), int(sl[3]))
