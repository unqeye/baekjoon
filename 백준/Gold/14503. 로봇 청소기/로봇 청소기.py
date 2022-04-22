N, M = map(int, input().split())
r, c, d = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]


def clean():
    global r, c, d
    table[r][c] = 2
    for i in range(4):
        if (d - i) % 4 == 0 and table[r][c - 1] == 0:
            c = c - 1
            d = 3
            clean()
        elif (d - i) % 4 == 1 and table[r - 1][c] == 0:
            r = r - 1
            d = 0
            clean()
        elif (d - i) % 4 == 2 and table[r][c + 1] == 0:
            c = c + 1
            d = 1
            clean()
        elif (d - i) % 4 == 3 and table[r + 1][c] == 0:
            r = r + 1
            d = 2
            clean()
    if d == 0 and table[r + 1][c] != 1:
        r = r + 1
        clean()
    elif d == 1 and table[r][c - 1] != 1:
        c = c - 1
        clean()
    elif d == 2 and table[r - 1][c] != 1:
        r = r - 1
        clean()
    elif d == 3 and table[r][c + 1] != 1:
        c = c + 1
        clean()
    else:
        return


clean()

count = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 2:
            count += 1

print(count)
