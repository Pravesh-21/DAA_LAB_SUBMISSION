def Longest_repeating_subsequence(s):
    n = len(s)
    list_lrs = []
    for i in range(0, n+1):
        row = [0]*(n+1)
        list_lrs.append(row)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                list_lrs[i][j] = list_lrs[i-1][j-1] + 1
            else:
                list_lrs[i][j] = max(list_lrs[i-1][j], list_lrs[i][j-1])
    
    return list_lrs

def LRS_printing(s, list_lrs):
    i = len(s)
    j = len(s)
    lrs_str = []
    
    while i > 0 and j > 0:
        if s[i-1] == s[j-1] and i != j:
            lrs_str.append(s[i-1])
            i -= 1
            j -= 1
        elif list_lrs[i-1][j] > list_lrs[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lrs_str.reverse()
    return ''.join(lrs_str)

s = input()
dp_table = Longest_repeating_subsequence(s)
print(dp_table[len(s)][len(s)])
print(LRS_printing(s, dp_table))
