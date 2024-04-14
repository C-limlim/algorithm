from copy import deepcopy

n, m, k = map(int, input().strip().split(" "))
board = [[[] for i in range(n + 1)]  for _ in range(n+1)]
peo_board = [[0] * (n+1) for _ in range(n+1)]
people = [[-1, -1, -1, -1]]
gun = [-1] + [0] * m
point = [-1] + [0] * m

for i in range(1, n + 1):
    row = [0] + list(map(int, input().strip().split(" ")))
    for j in range(1, n+ 1):
        if row[j] != 0:
            board[i][j].append(row[j])

for _ in range(m):
    people.append(list(map(int, input().strip().split(" "))))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

round = 1

def board_print(board):
    l = len(board)
    print("===============")
    for i in range(1, l):
        for j in range(1, l):
            print(board[i][j], end=" ")
        print()

def move(p_idx):
    global peo_board, people, direction
    x = people[p_idx][0]
    y = people[p_idx][1]
    dir_idx = people[p_idx][2]

    dx = x + direction[dir_idx][0]
    dy = y + direction[dir_idx][1]

    if dx < 1 or dx >= n +1 or dy < 1 or dy >= n+1:
        dir_idx = direction.index((-direction[dir_idx][0], -direction[dir_idx][1]))
        people[p_idx][2] = dir_idx
        dx = x + direction[dir_idx][0]
        dy = y + direction[dir_idx][1]

    people[p_idx][0] = dx
    people[p_idx][1] = dy
    peo_board[x][y] = 0

def take_gun(p_idx):
    '''
    이미 gun list에는 최소 1개의 gun이 있다. 그게 함수의 트리거 조건
    gun은 이미 sort 된 상태이다.
    '''
    global board, people
    g_score = gun[p_idx]
    x = people[p_idx][0]
    y = people[p_idx][1]

    gun_list = board[x][y]

    if gun_list[-1] > g_score:
        max_gun = gun_list.pop()
        if g_score != 0:
            gun_list.append(g_score)
        gun[p_idx] = max_gun

        gun_list.sort()
        board[x][y] = deepcopy(gun_list)

def fight(a):
    ax = people[a][0]
    ay = people[a][1]
    b = peo_board[ax][ay]

    #a와 b 모두 people, peo_board에 위치 업뎃 제대로 해야함
    a_score = people[a][3] + gun[a]
    b_score = people[b][3] + gun[b]
    winner = 0
    loser = 0

    if a_score > b_score:
        winner, loser = a, b
    elif a_score == b_score:
        if people[a][3] > people[b][3]:
            winner, loser = a, b
        else:
            winner, loser = b, a
    else:
        winner, loser = b, a

    #이긴 사람 포인트
    get_point = (people[winner][3] + gun[winner]) - (people[loser][3] + gun[loser])
    point[winner] += get_point

    #lose
    if gun[loser] != 0:
        #총 내려놓기
        loser_gun = gun[loser]
        gun[loser] = 0

        #총 보드에 넣어주기 - 정렬 잊으면 안됨
        lx = people[loser][0]
        ly = people[loser][1]
        gun_list = board[lx][ly]
        gun_list.append(loser_gun)
        gun_list.sort()
        board[lx][ly] = deepcopy(gun_list)

    #움직일 곳 찾음
    lx = people[loser][0]
    ly = people[loser][1]
    d_idx = people[loser][2]
    dx = lx + direction[d_idx][0]
    dy = ly + direction[d_idx][1]

    while dx < 1 or dx >= n+ 1 or dy < 1 or dy >= n+1 or peo_board[dx][dy] != 0:
        d_idx = (d_idx + 1) % 4
        dx = lx + direction[d_idx][0]
        dy = ly + direction[d_idx][1]

    people[loser][0], people[loser][1], people[loser][2] = dx, dy, d_idx
    peo_board[dx][dy] = loser

    if len(board[dx][dy]) != 0:
        take_gun(loser)

    #win
    wx = people[winner][0]
    wy = people[winner][1]
    if len(board[wx][wy]) > 0:
        take_gun(winner)
    peo_board[wx][wy] = winner


## 초기 세팅
for i in range(1, m+1):
    x = people[i][0]
    y = people[i][1]
    peo_board[x][y] = i


while round <= k:
    for i in range(1, m + 1):
        #print(i)
        #board_print(peo_board)
        move(i)
        x = people[i][0]
        y = people[i][1]
        if peo_board[x][y] == 0:
            peo_board[x][y] = i
            if len(board[x][y]) > 0:
                take_gun(i)
        else: #누군가 있따
            #print("fight")
            fight(i)
    round += 1

#board_print(peo_board)
#board_print(board)
#print("point")
for i in range(1, m + 1):
    print(point[i], end=" ")
