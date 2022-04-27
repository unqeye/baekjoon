from collections import deque

N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def turn(r, c, w):
    global grid
    new_grid = [[0 for _ in range(w)] for _ in range(w)]
    for i in range(w):
        for j in range(w):
            new_grid[i][j] = grid[r + w - 1 - j][c + i]
    for i in range(w):
        for j in range(w):
            grid[r + i][c + j] = new_grid[i][j]


def decrease_ice():
    global grid
    new_grid = [row[:] for row in grid]
    for r in range(2 ** N):
        for c in range(2 ** N):
            count = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and grid[nr][nc] > 0:
                    count += 1
            if count <= 2 and grid[r][c] > 0:
                new_grid[r][c] -= 1
    grid = [row[:] for row in new_grid]


for l in L:
    for r in range(0, 2 ** N, 2 ** l):
        for c in range(0, 2 ** N, 2 ** l):
            turn(r, c, 2 ** l)
    decrease_ice()

remain_ice = 0
for r in range(2 ** N):
    for c in range(2 ** N):
        remain_ice += grid[r][c]

biggest = 0
visit = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
for r in range(2 ** N):
    for c in range(2 ** N):
        if grid[r][c] > 0 and not visit[r][c]:
            count = 1
            visit[r][c] = True
            queue = deque([(r, c)])
            while queue:
                (cr, cc) = queue.popleft()
                for i in range(4):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and grid[nr][nc] > 0 and not visit[nr][nc]:
                        count += 1
                        visit[nr][nc] = True
                        queue.append((nr, nc))
            biggest = max(biggest, count)

print(remain_ice)
print(biggest)
