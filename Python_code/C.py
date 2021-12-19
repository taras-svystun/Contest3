def max_prefix_function(string: str) -> list:
    maximal = 0
    length = len(string)
    P = [0 for _ in range(length)]
    for i in range(1, length):
        j = P[i - 1]
        while j > 0 and string[i] != string[j]:
            j = P[j - 1]
        if string[i] == string[j]:
            j += 1
        P[i] = j
        if j > maximal:
            maximal = j
    return maximal


line = input()
print(max_prefix_function(line))
