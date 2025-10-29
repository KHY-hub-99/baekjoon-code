N = int(input())

sum = 1
count = 0
for i in range(1, 20000):
    if 3*((i)**2) - (3*(i)) + 1 < N:
        sum += 1
    elif 3*((i)**2) - (3*(i)) + 1 == N:
        count += i

if count == 0:
    print(sum)
else:
    print(count)