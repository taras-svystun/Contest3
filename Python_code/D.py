def palindrome(word: str) -> str:
    length = len(word)
    max_len, last = 1, length - 1
    max_pal, eventh = word[0], False
    for i in range(length - 1):
        cur_len, j = 0, length - 1
        cur_pal = []
        while i < j:
            if eventh and word[i] == word[j]:
                eventh = False
                break
            elif word[i] == word[j]:
                eventh = True
                break

        
        if cur_len > max_len:
            max_pal = cur_pal
            max_len = cur_len
    
    answer = [0 for _ in range(max_len)]
    for k in range(max_len // 2 + 1):
        if k + 1 == max_len - k:
            answer[k] = max_pal[k]
        else:
            print(k, max_len - k - 1, max_pal)
            answer[k], answer[max_len - k - 1] = max_pal[k], max_pal[k]
    return "".join(answer)

# case = input()
case = "qweeerq"
print(palindrome(case))
