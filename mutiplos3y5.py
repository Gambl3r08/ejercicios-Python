def solution(number):
    resto = 0
    for i in range(1, number):
        if i%3 == 0:
            resto += i
        if i%5 == 0:
            resto += i
    return resto
print(solution(91))