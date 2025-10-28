T = int(input())
C = [input() for _ in range(T)]
C_int = list(map(int, C))

L = [0 for _ in range(4)]
temp = []
for i in C_int:
    first = i // 25
    L[0] = L[0] + first
    first_surplus = i % 25
    second = first_surplus // 10
    L[1] = L[1] + second
    second_surplus = first_surplus % 10
    third = second_surplus // 5
    L[2] = L[2] + third
    third_surplus = second_surplus % 5
    fourth = third_surplus // 1
    L[3] = L[3] + fourth
    temp.append(L)
    L = [0 for _ in range(4)]

for i in temp:
    print(" ".join(map(str, i)))