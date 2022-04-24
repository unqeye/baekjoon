import copy
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def get_block_groups(grid):
    grid = copy.deepcopy(grid)
    block_visit = [[False for _ in range(N)] for _ in range(N)]
    block_groups = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] is not None and grid[r][c] > 0 and not block_visit[r][c]:
                block_visit[r][c] = True
                count, rainbow = 1, 0
                blocks = []
                visit = [[False for _ in range(N)] for _ in range(N)]
                visit[r][c] = True
                queue = deque([(r, c)])
                while queue:
                    (cr, cc) = queue.popleft()
                    blocks.append((cr, cc))
                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]
                        if (0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and
                                (grid[nr][nc] == 0 or grid[nr][nc] == grid[r][c])):
                            if grid[nr][nc] == grid[r][c]:
                                grid[nr][nc] = -1
                            visit[nr][nc] = True
                            queue.append((nr, nc))
                            count += 1
                            if grid[nr][nc] == 0:
                                rainbow += 1
                if count >= 2:
                    block_groups.append((count, rainbow, r, c, blocks))
    return block_groups


def gravity():
    new_grid = copy.deepcopy(grid)
    for _ in range(N - 1):
        for r in range(N - 1, 0, -1):
            for c in range(N):
                if new_grid[r][c] is None and new_grid[r - 1][c] is not None and new_grid[r - 1][c] != -1:
                    new_grid[r][c] = new_grid[r - 1][c]
                    new_grid[r - 1][c] = None
    grid[:] = new_grid


def rotate_left():
    new_grid = [[None for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_grid[r][c] = grid[c][N - 1 - r]
    grid[:] = new_grid


ans = 0
while True:
    block_groups = get_block_groups(grid)
    if len(block_groups) == 0:
        break
    block_groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    for (r, c) in block_groups[0][4]:
        grid[r][c] = None
    ans += block_groups[0][0] ** 2
    gravity()
    rotate_left()
    gravity()

print(ans)
