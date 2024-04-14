from collections import deque
from copy import deepcopy
n, m, k = map(int, input().strip().split(" "))

shell = []
for _ in range(n):
    shell.append(list(map(int, input().strip().split(" "))))
latest_att = [[0] * m for _ in range(n)]
involved = [[0] * m for _ in range(n)]
remain_shell = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] #우하좌상

def game_over():
    '''
    1 이상 shell의 개수를 리턴
    '''
    global shell
    count = 0
    for i in range(n):
        for j in range(m):
            if shell[i][j] > 0:
                count += 1

    return count

def find_weak():
    global shell, latest_att
    weak = 5001
    idx = []
    for i in range(n):
        for j in range(m):
            power = shell[i][j]
            if power == 0:
                continue
            if power < weak:
                weak = power
                idx = [(i, j)]
            elif power == weak:
                idx.append((i, j))
    #1. 제일 공격력 낮은 친구 리턴.
    if len(idx) == 1:
        return idx[0]

    latest = [0] * len(idx)
    all_same = True
    for i, pos in enumerate(idx):
        latest[i] = latest_att[pos[0]][pos[1]]
        if i > 0:
            prev = i - 1
            if latest[prev] != latest[i]:
                all_same = False

    #2. 가장 최근 친구 리턴
    if not all_same:
        big_latest = latest[0]
        big_idx = 0
        for i, lat in enumerate(latest):
            if big_latest < lat:
                big_latest = lat
                big_idx = i

        return idx[big_idx]

    sum_rc = [0] * len(idx)
    all_same = True
    for i, pos in enumerate(idx):
        sum_rc[i] = pos[0] + pos[1]
        if i > 1:
            prev = i - 1
            if sum_rc[i] != sum_rc[prev]:
                all_same = False

    #3. 행과 열의 합이 제일 큰걸 리턴
    if not all_same:
        big_rc = sum_rc[0]
        rc_idx = 0
        for i, rc in enumerate(sum_rc):
            if big_rc < rc:
                big_rc = rc
                rc_idx = i
        return idx[rc_idx]

    #4. 열이 제일 큰걸 리턴
    col = idx[0][1]
    col_idx = 0
    for i, pos in enumerate(idx):
        if col < pos[1]:
            col = pos[1]
            col_idx = i

    return idx[col_idx]

def find_strong():
    global shell, latest_att
    strong = 0
    idx = []
    for i in range(n):
        for j in range(m):
            if shell[i][j] == 0:
                continue
            if shell[i][j] > strong:
                strong = shell[i][j]
                idx = [(i, j)]
            elif shell[i][j] == strong:
                idx.append((i, j))

    #1. 공격력 제일 센 친구 리턴
    if len(idx) == 1:
        return idx[0]

    latest = [0] * len(idx)
    all_same = True
    for i, pos in enumerate(idx):
        latest[i] = latest_att[pos[0]][pos[1]]
        if i > 0:
            prev = i - 1
            if latest[prev] != latest[i]:
                all_same = False

    #2. 가장 공격 안한(값이 작은) 친구 리턴
    if not all_same:
        small_latest = latest[0]
        small_idx = 0
        for i, lat in enumerate(latest):
            if lat < small_latest:
                small_latest = lat
                small_idx = i
        return idx[small_idx]

    sum_rc = [0] * len(idx)
    all_same = True
    for i, pos in enumerate(idx):
        sum_rc[i] = pos[0] + pos[1]
        if i > 0:
            prev = i - 1
            if sum_rc[i] != sum_rc[prev]:
                all_same = False

    #이것도 생각해보면 행열합 같은놈들만 또 뺴줘야하잔아? 그냥 정렬이 낫겠다..
    #3. 행열합 가장 작은걸 리턴
    if not all_same:
        small_rc = sum_rc[0]
        small_idx = 0
        for i, rc in enumerate(sum_rc):
            if rc < small_rc:
                small_rc = rc
                small_idx = i
        return idx[small_idx]

    #4. 열이 제일 작은걸 리턴
    col = idx[0][1]
    col_idx = 0
    for i, pos in enumerate(idx):
        if col > pos[1]:
            col = pos[1]
            col_idx = i
    return idx[col_idx]

def attack(wx, wy, sx, sy):
    '''
    week, strong 두개 받아 attack함
    '''
    global involved, shell, latest_att, round
    laser = False
    visited = [[0] * m for _ in range(n)]

    elm = [[(wx, wy)], 0]
    q = deque()
    q.append(elm)
    visited[wx][wy] = 1
    ans_route = []

    #attack 했음을 표시
    latest_att[wx][wy] = round

    while q:
        route = q.popleft()
        mv = route[1]
        x, y = route[0][-1]
        visited[x][y] = 1
        if x == sx and y == sy:
            ans_route.append(route)
            laser = True
            continue

        for i in range(4):
            dx = (x + direction[i][0] + n) % n
            dy = (y + direction[i][1] + m) % m
            if shell[dx][dy] != 0 and visited[dx][dy] != 1:
                new_route = route[0] + [(dx, dy)]
                new_route = [new_route, mv + 1]
                q.append(new_route)

    if laser:
        best_route = ans_route[0][1]
        best_idx = 0
        for i, route in enumerate(ans_route):
            if route[1] < best_route:
                best_route = route[1]
                best_idx = i
        ans_route = ans_route[best_idx]

        middle = ans_route[0][1:-1]
        power = n + m + shell[wx][wy]
        shell[sx][sy] -= power
        for _, pos in enumerate(middle):
            shell[pos[0]][pos[1]] -= power // 2

        #involved에 표시
        for _, pos in enumerate(ans_route[0]):
            involved[pos[0]][pos[1]] = 1

        shell[wx][wy] = power

    else:
        involved[wx][wy] = 1
        power = n + m + shell[wx][wy]
        shell[wx][wy] = power

        for i in range(sx - 1, sx + 2):
            for j in range(sy - 1, sy + 2):
                dx = (i + n) % n
                dy = (j + m) % m
                if shell[dx][dy] == 0:
                    continue
                if wx == dx and wy == dy:
                    continue
                if dx == sx and dy == sy:
                    shell[dx][dy] -= power
                    involved[dx][dy] = 1
                else:
                    shell[dx][dy] -= power // 2
                    involved[dx][dy] = 1

def crash():
    '''
    0 이하의 board는 0으로 처리
    '''
    global shell
    for i in range(n):
        for j in range(m):
            if shell[i][j] < 0:
                shell[i][j] = 0

def fix():
    global shell, involved

    for i in range(n):
        for j in range(m):
            if not involved[i][j]:
                if shell[i][j] > 0:
                    shell[i][j] += 1

def board_print(board):
    row = len(board)
    col = len(board[0])
    print("+++++++++++")
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=" ")
        print()

remain_shell = game_over()
round = 1

while remain_shell > 1 and round <= k:
    print(round)
    wx, wy = find_weak()
    sx, sy = find_strong()
    attack(wx, wy, sx, sy)
    crash()
    remain_shell = game_over()
    if remain_shell == 1:
        break
    fix()
    print(wx, wy, sx, sy)
    board_print(shell)
    involved = [[0] * m for _ in range(n)]
    round += 1

#가장 강한 포탑의 공격력 출력
ans = shell[0][0]
for i in range(n):
    for j in range(m):
        if shell[i][j] > ans:
            ans = shell[i][j]

print(ans)
