D = [input().split() for _ in range(20)]
grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
school = dict(zip(grade, score))

sum = 0
count = 0
for i in range(20):
  if D[i][2] in school:
    count += float(D[i][1])
    value =  school[D[i][2]]*float(D[i][1])
    sum += value


print(sum/count)