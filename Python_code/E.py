def z_to_prefix(array: list, length: int) -> list:
    i = 1
    converted = [0 for _ in range(length)]
    while i < length:
        if array[i]:
            j = array[i] - 1
            while j >= 0 and not converted[i + j]:
                converted[i + j] = j + 1
                j -= 1
        i += 1
    return converted


n = int(input())
z = list(map(int, input().split()))
print(" ".join(map(str, z_to_prefix(z, n))))