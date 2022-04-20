n = int(input())
nodes = [() for _ in range(n + 1)]
for _ in range(n):
    cur, l, r = map(int, input().split())
    nodes[cur] = (l, r)

child = [False for _ in range(n + 1)]
for (l, r) in nodes[1:]:
    if l != -1:
        child[l] = True
    if r != -1:
        child[r] = True

root = 0
for i in range(1, n + 1):
    if not child[i]:
        root = i

col = 1
pos = [[] for _ in range(n + 1)]


def inorder(lev, cur):
    global col
    (l, r) = nodes[cur]
    if l != -1:
        inorder(lev + 1, l)
    pos[lev].append(col)
    col += 1
    if r != -1:
        inorder(lev + 1, r)


inorder(1, root)

level = 0
width = 0
for i in range(1, n + 1):
    maxCol = 0
    minCol = 1e9
    for col in pos[i]:
        maxCol = max(maxCol, col)
        minCol = min(minCol, col)
    curWidth = maxCol - minCol + 1
    if width < curWidth:
        level = i
        width = curWidth

print(level, width)
