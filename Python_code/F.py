def prefix_to_z(array: list, length: int) -> list:
    converted = [0 for _ in range(length)]
    i = 1
    while i < length:
        if array[i]:
            converted[i - array[i] + 1] = array[i]
        i += 1
    converted[0] = length

    if converted[1]:
        j = 1
        while j < converted[1]:
            converted[j + 1] = converted[1] - j
            j += 1

    for i in range(converted[1] + 1, i < length - 1):
        helper = i
        if converted[i] and not converted[i + 1]:
            j = 1
            while j < converted[i] and converted[i + j] <= converted[j]:
                converted[i + j] = min(converted[j], converted[i] - j)
                helper = i + j
                j += 1
            if helper - k:
                k = helper
            else:
                k += 1

    return converted


n = int(input())
prefix = list(map(int, input().split()))
print(" ".join(map(str, prefix_to_z(prefix, n))))
# t = "0 0 1 0 1 2 3 1"
# n = 8
# prefix = list(map(int, t.split()))
# print(" ".join(map(str, prefix_to_z(prefix, n))))
