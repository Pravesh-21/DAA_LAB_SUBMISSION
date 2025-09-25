def Shortest_lenght_LCS(x, y):
    n = len(x)
    m = len(y)
    list_lcs = []
    for i in range(0, n+1):
        row = [0]*(m+1)
        list_lcs.append(row)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                list_lcs[i][j] = list_lcs[i-1][j-1] + 1
            else:
                list_lcs[i][j] = max(list_lcs[i-1][j], list_lcs[i][j-1])
    return list_lcs

def Length_printing(x, y, list_lcs):
    i = len(x)
    j = len(y)
    list_str = []
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            list_str.append(x[i-1])
            i -= 1
            j -= 1
        elif list_lcs[i-1][j] > list_lcs[i][j-1]:
            i -= 1
        else:
            j -= 1
    list_str.reverse()
    return ''.join(list_str)

s1 = input()
s2 = input()
lcs_table = Shortest_lenght_LCS(s1, s2)
print("Length of LCS:", lcs_table[len(s1)][len(s2)])
print("LCS string:", Length_printing(s1, s2, lcs_table))
