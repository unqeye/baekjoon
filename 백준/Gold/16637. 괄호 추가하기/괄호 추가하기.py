N = int(input())
exp = list(input())


def calc(_exp):
    global ans
    _exp = [c for c in _exp if c]
    cur = _exp[0]
    for i in range(2, len(_exp), 2):
        cur = str(eval(cur + _exp[i - 1] + _exp[i]))
    ans = max(ans, int(cur))


def dfs(_exp, _pos):
    calc(_exp[:])
    if _pos >= N:
        return
    dfs(_exp[:], _pos + 2)
    if _pos + 2 < len(_exp):
        dfs(_exp[:_pos] + [str(eval(''.join(_exp[_pos:_pos + 3]))), '', ''] + _exp[_pos + 3:], _pos + 4)


ans = -(2 ** 31)
dfs(exp[:], 0)

print(ans)
