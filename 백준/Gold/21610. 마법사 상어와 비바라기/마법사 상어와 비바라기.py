N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
move = [tuple(map(int, input().split())) for _ in range(M)]
cloud = [[False for _ in range(N)] for _ in range(N)]
cloud[N - 1][0] = cloud[N - 1][1] = cloud[N - 2][0] = cloud[N - 2][1] = True
D = [(1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]

for (d, s) in move:
    # 1. 구름 이동
    (dr, dc) = D[d % 8]
    moved_cloud = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if cloud[r][c]:
                moved_cloud[(r + s * dr) % N][(c + s * dc) % N] = True
    # 2. 바구니에 저장된 물의 양 1 증가
    copy_water = []
    for r in range(N):
        for c in range(N):
            if moved_cloud[r][c]:
                copy_water.append((r, c))
                grid[r][c] += 1
    # 3. 구름이 모두 사라짐
    # 4. 물복사버그 마법 시전
    for (r, c) in copy_water:
        for i in [0, 2, 4, 6]:
            (dr, dc) = D[i]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                grid[r][c] += 1
    # 5. 물의 양이 2 이상인 칸에 구름이 생기고, 물의 양 2 감소
    new_cloud = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if grid[r][c] >= 2 and not moved_cloud[r][c]:
                new_cloud[r][c] = True
                grid[r][c] -= 2
    cloud[:] = [row[:] for row in new_cloud]

total = 0
for r in range(N):
    for c in range(N):
        total += grid[r][c]

print(total)
