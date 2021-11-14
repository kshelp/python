import time

draw = 0
win = 0
lose = 0

while True:    
    user = int(input("0(가위), 1(바위), 2(보) : "))
    comp = int( time.time() * 1000 % 3)

    result = comp - user

    if result == 0: 
        print("비겼습니다.")
        draw += 1
    elif result in [2, -1]:
        print("사용자가 이겼습니다.")
        win += 1
    else:
        print("컴퓨터가 이겼습니다.")
        lose += 1

    con = input("게임을 계속하시겠습니까? (y/n)")
    if con in ['N', 'n']:
        break

print("당신은 {0}전 {1}승 {2}무 {3}패 입니다.".format(draw+win+lose, win, draw, lose))
