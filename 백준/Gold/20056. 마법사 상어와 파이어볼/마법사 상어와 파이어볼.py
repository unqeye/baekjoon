N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r - 1][c - 1].append([m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def get_new_ds(ds):
    even = True
    for i in ds:
        if i % 2 != 0:
            even = False
            break
    odd = True
    for i in ds:
        if i % 2 != 1:
            odd = False
            break
    if even or odd:
        return [0, 2, 4, 6]
    else:
        return [1, 3, 5, 7]


def move():
    global grid
    new_grid = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                for [m, s, d] in grid[r][c]:
                    new_r = (r + s * dr[d]) % N
                    new_c = (c + s * dc[d]) % N
                    new_grid[new_r][new_c].append([m, s, d])
    for r in range(N):
        for c in range(N):
            if len(new_grid[r][c]) >= 2:
                new_m, new_s = 0, 0
                ds = []
                for [m, s, d] in new_grid[r][c]:
                    new_m += m
                    new_s += s
                    ds.append(d)
                new_m //= 5
                new_s //= len(new_grid[r][c])
                new_dirs = get_new_ds(ds)
                new_grid[r][c].clear()
                if new_m > 0:
                    for new_d in new_dirs:
                        new_grid[r][c].append([new_m, new_s, new_d])
    grid = new_grid


for _ in range(K):
    move()

ans = 0
for r in range(N):
    for c in range(N):
        if grid[r][c]:
            for [m, d, s] in grid[r][c]:
                ans += m

print(ans)
