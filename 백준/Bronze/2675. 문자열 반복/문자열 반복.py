T = int(input())
R = [input().split() for _ in range(T)]

repeat_string = ""
for i in range(len(R)):
    repeat = int(R[i][0])
    string = R[i][1]
    for j in string:
        repeat_string += j*repeat
    repeat_string += "\n"

print(repeat_string)