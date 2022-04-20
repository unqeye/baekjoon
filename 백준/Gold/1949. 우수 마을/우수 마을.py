import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
population = [0] + list(map(int, input().split()))
adjacent = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    adjacent[x] += [y]
    adjacent[y] += [x]

visit = [False for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]


def dfs(cur):
    visit[cur] = True
    dp[cur][1] = population[cur]
    for i in adjacent[cur]:
        if not visit[i]:
            dfs(i)
            dp[cur][0] += max(dp[i][0], dp[i][1])
            dp[cur][1] += dp[i][0]


dfs(1)
print(max(dp[1][0], dp[1][1]))
