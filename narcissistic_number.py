def find_narcissistic_number(start: int, end: int) -> list:
    result = []
    for i in range(start, end):
        digit = 1
        tmp = i
        while tmp // 10 > 0:
            digit = digit + 1
            tmp = tmp // 10
        cnt = 0
        tmp = i
        for j in range(digit):
            cnt = cnt + pow(tmp % 10, digit)
            tmp = tmp // 10
        if cnt == i:
            result.append(i)
    return result
