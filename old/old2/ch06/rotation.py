# rotation 
# 2,3,5,6
# 9,5,9,3

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

# random은 난수를 발생시키는 모듈이다.
import random
#num = random.randint(1,10)  # 1~10사이의 정수중에서 난수값을 리턴

test = [[0]*11 for i in range(10)]
print(test)
#test = [[1,2,3], [4,5,6], [7,8,9]]

cnt = 'y'

while (cnt=='y' or cnt=='Y'):
    choice = int(input("90도 회전할 방향을 선택하세요(오른쪽:1, 왼쪽:2):"))
    if(choice==1):
        print(rotate_90(test))
    if(choice==2):
        print(rotate_90(test))
    
    cnt = input("계속하시겠습니까? (y/n) ")

    

