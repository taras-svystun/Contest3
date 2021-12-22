def is_palindrome(word: str, length: int) -> bool:
    for i in range(length // 2 + 1):
        if word[i] != word[length - i - 1]:
            return False
    return True

def square_palindrome(square: list, height: int, width: int) -> str:
    answer = [0, 0, 0, 0]
    up, down, left, right = answer
    while up < height and right < width:

        

    return " ".join(answer)

h, w = list(map(int, input().split()))
matrix = []
for _ in range(h):
    matrix.append(list(input()))

for el in matrix:
    print(el)