def max_power_prefix(string: str) -> int:
    length = len(string)
    i = 1
    while i < length // 2:
        prefix = string[:i]
        start, finish = i, 2 * i
        while finish < length and prefix == string[start:finish]:
            start += i
            finish += i

        if finish == length and string[start:finish] == prefix:
            return length // i
        i += 1
    return 1

tests = []
while 1:
    try:
        tests.append(input())
    except:
        break


for test in tests:
    print(max_power_prefix(test))
