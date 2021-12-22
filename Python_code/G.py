def is_palindrome(word: str, length: int) -> bool:
    for i in range(length // 2 + 1):
        if word[i] != word[length - i - 1]:
            return False
    return True

def palindrome(word: str, length: int) -> str:
    for i in range(length - 1):
        selected = word[i:]
        if is_palindrome(selected, length - i - 1):
            return i + 1
    return length - 1



# n = int(input())
# case = input()
n = 15
case = "murderforajarof"
max_pal = max(
    palindrome(case, n),
    palindrome(case[::-1], n)
)
print(n - max_pal)