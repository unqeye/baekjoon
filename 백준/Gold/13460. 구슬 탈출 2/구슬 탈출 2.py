from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'
        if board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
queue = deque()
visit[red[0]][red[1]][blue[0]][blue[1]] = True
queue.append((1, red, blue))
while queue:
    (count, red, blue) = queue.popleft()
    if count > 10:
        break
    for (dx, dy) in d:
        (rx, ry) = red
        (bx, by) = blue
        while True:
            if board[rx + dx][ry + dy] == '.':
                rx += dx
                ry += dy
            elif board[rx + dx][ry + dy] == 'O':
                rx += dx
                ry += dy
                break
            else:
                break
        while True:
            if board[bx + dx][by + dy] == '.':
                bx += dx
                by += dy
            elif board[bx + dx][by + dy] == 'O':
                bx += dx
                by += dy
                break
            else:
                break
        if rx == bx and ry == by and board[rx][ry] != 'O':
            dr = abs(rx - red[0]) + abs(ry - red[1])
            db = abs(bx - blue[0]) + abs(by - blue[1])
            if dr > db:
                rx -= dx
                ry -= dy
            elif db > dr:
                bx -= dx
                by -= dy
        if board[bx][by] != 'O':
            if board[rx][ry] == 'O':
                print(count)
                quit()
            elif not visit[rx][ry][bx][by]:
                visit[rx][ry][bx][by] = True
                queue.append((count + 1, (rx, ry), (bx, by)))

print(-1)
