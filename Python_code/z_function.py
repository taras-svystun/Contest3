def z_function(string: str) -> list:
    length = len(string)
    Z = [0 for _ in range(length)]
    i = 1
    left, right = 0, 0
    while i < length:
        if i < right:
            Z[i] = min(right - i + 1, Z[i - left])
        while i + Z[i] < length and string[Z[i]] == string[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > right:
            left, right = i, i + Z[i] - 1
        i += 1
    return Z
