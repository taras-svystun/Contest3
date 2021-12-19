def prefix_function(line: str) -> list:
    length = len(line)
    P = [0 for _ in range(length)]
    for i in range(1, length):
        j = P[i - 1]
        while j > 0 and line[i] != line[j]:
            j = P[j - 1]
        if line[i] == line[j]:
            j += 1
        P[i] = j
    return P


start = input()
end = input()
print(prefix_function(end + start)[-1])
