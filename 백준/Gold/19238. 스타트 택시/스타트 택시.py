from collections import deque

N, M, fuel = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            table[i][j] = -1
cr, cc = map(int, input().split())
cr -= 1
cc -= 1
dest = [(0, 0)]
for i in range(1, M + 1):
    sr, sc, er, ec = map(int, input().split())
    table[sr - 1][sc - 1] = i
    dest.append((er - 1, ec - 1))

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for _ in range(M):
    customer = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[cr][cc] = True
    queue = deque([(cr, cc, 0)])
    while queue:
        cr, cc, dist = queue.popleft()
        if table[cr][cc] > 0:
            customer.append((cr, cc, dist, table[cr][cc]))
        for (dr, dc) in d:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and table[nr][nc] != -1:
                visit[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    if len(customer) == 0:
        print(-1)
        quit()
    customer.sort(key=lambda x: (x[2], x[0], x[1]))
    cr, cc, dist, customerIndex = customer[0]
    table[cr][cc] = 0
    fuel -= dist
    if fuel <= 0:
        print(-1)
        quit()
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[cr][cc] = True
    queue = deque([(cr, cc, 0)])
    while queue:
        cr, cc, dist = queue.popleft()
        if (cr, cc) == dest[customerIndex]:
            fuel -= dist
            if fuel < 0:
                print(-1)
                quit()
            fuel += 2 * dist
            customerIndex = 0
            break
        for (dr, dc) in d:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and table[nr][nc] != -1:
                visit[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    if customerIndex != 0:
        print(-1)
        quit()

print(fuel)
