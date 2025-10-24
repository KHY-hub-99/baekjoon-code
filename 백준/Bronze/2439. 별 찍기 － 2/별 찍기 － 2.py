N = int(input())
num = [x for x in range(0, N)]
for i in range(1, N+1):
    print(f'{" "*num[-i]}' + f'{"*"*i}')