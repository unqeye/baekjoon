N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


def baseball(_order):
    batter = 0
    score = 0
    for inning in range(N):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            if data[inning][_order[batter]] == 0:
                out += 1
            elif data[inning][_order[batter]] == 1:
                score += base3
                base3, base2, base1 = base2, base1, 1
            elif data[inning][_order[batter]] == 2:
                score += base3 + base2
                base3, base2, base1 = base1, 1, 0
            elif data[inning][_order[batter]] == 3:
                score += base3 + base2 + base1
                base3, base2, base1 = 1, 0, 0
            elif data[inning][_order[batter]] == 4:
                score += base3 + base2 + base1 + 1
                base3 = base2 = base1 = 0
            batter = (batter + 1) % 9
    global ans
    ans = max(ans, score)


def dfs(_count, _visit, _order):
    if _count == 9:
        baseball(_order)
        return
    if _count == 3:
        dfs(_count + 1, _visit[:], _order + [0])
    else:
        for i in range(9):
            if not _visit[i]:
                __visit = _visit[:]
                __visit[i] = True
                dfs(_count + 1, __visit, _order + [i])


ans = 0
dfs(0, [True] + [False for _ in range(8)], [])

print(ans)
