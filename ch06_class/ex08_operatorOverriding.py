class HousePark:
    lastname = "박"
    def __init__(self,name): # 생성자
        self.fullname = self.lastname + name
    def travel(self,where):
        print("%s, %s여행을 가다." %(self.fullname,where))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네." %(self.fullname, other.fullname))
    def __add__(self, other): # '+' 연산자 오버로딩 정의
        print("%s, %s 결혼했네." %(self.fullname, other.fullname))
        
class HouseKim(HousePark):
    lastname = "김"
    # 메서드 오버라이딩(method overriding): 재정의
    def travel(self,where,day):
        print("%s, %s여행 %d일 가네." %(self.fullname,where,day))
        
pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet