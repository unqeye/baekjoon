N, M, x, y, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
op = list(map(int, input().split()))

top = 0
front = 0
down = 0
back = 0
left = 0
right = 0

for d in op:
    if d == 1 and y + 1 < M:
        y += 1
        top, front, down, back, left, right = left, front, right, back, down, top
    elif d == 2 and 0 <= y - 1:
        y -= 1
        top, front, down, back, left, right = right, front, left, back, top, down
    elif d == 3 and 0 <= x - 1:
        x -= 1
        top, front, down, back, left, right = front, down, back, top, left, right
    elif d == 4 and x + 1 < N:
        x += 1
        top, front, down, back, left, right = back, top, front, down, left, right
    else:
        continue
    if table[x][y] == 0:
        table[x][y] = down
    else:
        down = table[x][y]
        table[x][y] = 0
    print(top)
