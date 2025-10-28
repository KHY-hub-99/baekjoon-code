N, B = map(int, input().split())
dic = {k: v for k, v in zip([str(i) for i in range(0, 10)] + [chr(i) for i in range(65, 91)], range(0, 36))}

value = []
while N > 0:
    value.append(N % B)
    N = N // B
    
result = []
for val in value[::-1]:
    for k, v in dic.items():
        if v == val:
            result.append(k)
print("".join(result))