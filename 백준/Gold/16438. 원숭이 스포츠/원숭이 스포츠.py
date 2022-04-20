n = int(input())
arr = [[False for _ in range(n)] for _ in range(8)]


def divide_and_conquer(day, left, right):
    if day == 8:
        return
    mid = (left + right) // 2
    for i in range(left, mid):
        arr[day][i] = not arr[day - 1][i]
    for i in range(mid, right):
        arr[day][i] = arr[day - 1][i]
    divide_and_conquer(day + 1, left, mid)
    divide_and_conquer(day + 1, mid, right)


divide_and_conquer(1, 0, n)

for l in arr[1:]:
    for b in l:
        if b:
            print('A', end='')
        else:
            print('B', end='')
    print()
