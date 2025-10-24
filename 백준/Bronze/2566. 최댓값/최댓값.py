D = [input().split() for _ in range(9)]
D_int = [list(map(int, i)) for i in D]
M = max(map(max, D_int))

L = []
for i in range(9):
    for j in range(9):
        if D_int[i][j] == M:
            L.append(i+1)
            L.append(j+1)

print(M)
print(L[0],L[1])