import random

data = [["청기", "백기", "둘다"], ["올", "내"], ["려","려","리지마"]]
answer = [[1,3,2], [4,6], []]

i = "y"
sum = 0
rate = 0
num = 0

while True:
    if i == "n": 
        break
    print(*[random.choice(d) for d in data], sep='')
    i = input(": ")
    num += 1


    
