def longest_consec(strarr:list, k:int):
    n = len(strarr) 
    if k > n or k <= 0 or n == 0:
        return ""
    
    len_ = []
    n = n if k == 1 else n-1
    for l in range(0, n):
        s = []
        x = ''
        y = 0
        for i in range(l, l+k):
            x += strarr[i]
            y += len(strarr[i])
        s.append(y)
        s.append(x)
        len_.append(s[:])

    return max(len_, key=lambda x: x[0])[1] 

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))