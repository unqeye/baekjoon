import copy

fish_table = [[None for _ in range(4)] for _ in range(4)]
shark = []

for r in range(4):
    line = list(map(int, input().split()))
    for c in range(4):
        fish_no, fish_dir = line[2 * c], line[2 * c + 1] - 1
        fish_table[r][c] = [fish_no, fish_dir]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(fish_table, shark, cur):
    for fish_no in range(1, 17):
        fish_r, fish_c = -1, -1
        for r in range(4):
            for c in range(4):
                if fish_table[r][c] and fish_table[r][c][0] == fish_no:
                    fish_r, fish_c = r, c
                    break
        if fish_r >= 0 and fish_c >= 0:
            fish_dir = fish_table[fish_r][fish_c][1]
            for i in range(8):
                next_r = fish_r + dr[(fish_dir + i) % 8]
                next_c = fish_c + dc[(fish_dir + i) % 8]
                if 0 <= next_r < 4 and 0 <= next_c < 4:
                    if shark[0] != next_r or shark[1] != next_c:
                        fish_table[fish_r][fish_c] = fish_table[next_r][next_c]
                        fish_table[next_r][next_c] = [fish_no, (fish_dir + i) % 8]
                        break
    [shark_r, shark_c, shark_dir] = shark
    for i in range(1, 4):
        next_r = shark_r + i * dr[shark_dir]
        next_c = shark_c + i * dc[shark_dir]
        if not 0 <= next_r < 4 or not 0 <= next_c < 4:
            break
        if fish_table[next_r][next_c]:
            new_fish_table = copy.deepcopy(fish_table)
            [eat_no, eat_dir] = new_fish_table[next_r][next_c]
            new_shark = [next_r, next_c, eat_dir]
            new_fish_table[next_r][next_c] = None
            global ans
            ans = max(ans, cur + eat_no)
            dfs(new_fish_table, new_shark, cur + eat_no)


[eat_no, eat_dir] = fish_table[0][0]
shark = [0, 0, eat_dir]
fish_table[0][0] = None

ans = eat_no
dfs(fish_table, shark, eat_no)

print(ans)
