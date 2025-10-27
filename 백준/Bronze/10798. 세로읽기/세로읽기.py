data = [input().split() for _ in range(5)]
L = []
for i in data:
    length = len(i[0])
    L.append(length)

max_length = max(L)

for j in range(max_length):
    result = ""
    for i in range(len(data)):
        try:
            result += data[i][0][j]
        except IndexError:
            pass
    print(result, end="")