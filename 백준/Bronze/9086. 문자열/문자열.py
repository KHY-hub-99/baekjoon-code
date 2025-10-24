T = int(input())
D = [input().split() for _ in range(T)]

for i in range(len(D)):
    print(f"{D[i][0][0]}{D[i][0][-1]}")