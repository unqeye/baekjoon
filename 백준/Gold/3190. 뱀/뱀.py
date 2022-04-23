from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2

L = int(input())
move = deque()
for _ in range(L):
    x, c = input().split()
    x = int(x)
    move.append((x, c))

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curDir = 1
snake = deque()
snake.append((0, 0))
board[0][0] = 1
sec = 0
while True:
    sec += 1
    (headR, headC) = snake[-1]
    (dr, dc) = d[curDir]
    if 0 <= headR + dr < N and 0 <= headC + dc < N and board[headR + dr][headC + dc] != 1:
        if board[headR + dr][headC + dc] == 0:
            (tailR, tailC) = snake.popleft()
            board[tailR][tailC] = 0
        snake.append((headR + dr, headC + dc))
        board[headR + dr][headC + dc] = 1
    else:
        break
    if move and move[0][0] == sec:
        if move[0][1] == 'L':
            curDir = (curDir - 1) % 4
        else:
            curDir = (curDir + 1) % 4
        move.popleft()

print(sec)
