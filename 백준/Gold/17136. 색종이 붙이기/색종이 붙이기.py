table = [list(map(int, input().split())) for _ in range(10)]


def able(_x, _y, _width, _table):
    if _x + _width - 1 >= 10 or _y + _width - 1 >= 10:
        return False
    for dx in range(_width):
        for dy in range(_width):
            if _table[_x + dx][_y + dy] == 0:
                return False
    return True


def fill(_x, _y, _width, _table):
    for dx in range(_width):
        for dy in range(_width):
            _table[_x + dx][_y + dy] = 0
    return


def dfs(_table, _paper):
    for x in range(10):
        for y in range(10):
            if _table[x][y] == 1:
                for width in range(1, 6):
                    if able(x, y, width, _table):
                        if _paper[width - 1] < 5:
                            __table = [row[:] for row in _table]
                            fill(x, y, width, __table)
                            __paper = _paper[:]
                            __paper[width - 1] += 1
                            dfs(__table, __paper)
                return
    global ans
    ans = min(ans, sum(_paper))


ans = 1e9
dfs(table, [0, 0, 0, 0, 0])

if ans == 1e9:
    print(-1)
else:
    print(ans)
