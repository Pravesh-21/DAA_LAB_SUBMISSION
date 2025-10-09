import math
def Optimal_Binary_Search_Tree(keys, prob, n):
    e = []
    w = []
    for i in range(n+2):
        e.append([0]*(n+2))
        w.append([0]*(n+2))
    for i in range(1, n+2):
        e[i][i-1] = prob[i-1]
        w[i][i-1] = prob[i-1]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + keys[j-1] + prob[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
    return round(e[1][n])

n = int(input('Enter the size of the succesful array keys:-'))
m = int(input('Enter the size of the unsuccesful array keys:-'))
p = []
q = []
print('Enter the elements for succesful keys:-')
for i in range(n):
    x = float(input())
    p.append(x)
print('Enter the elements for unsuccesful serach between keys:-')
for i in range(m):
    y = float(input())
    q.append(y)

length = len(p)
print(Optimal_Binary_Search_Tree(p, q, length))
