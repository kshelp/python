def gugudan(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(gugudan(2))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

print(gugudan(9))
# [9, 18, 27, 36, 45, 54, 63, 72, 81]
