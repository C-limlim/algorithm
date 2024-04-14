from copy import deepcopy

n, m, k = map(int,input().strip().split(" "))
board = []
people = [] #x, y, finish
for _ in range(n):
    board.append(list(map(int, input().strip().split(" "))))
for _ in range(m):
    pos = list(map(int, input().strip().split(" ")))
    people.append([pos[0] -1] + [pos[1] - 1] + [0])
exit = list(map(int, input().strip().split(" ")))
exit[0] -= 1
exit[1] -= 1
exit_people = 0
time = 1
move = 0

def people_print(people):
    for i in range(m):
        print(i,":", "pos-", people[i][:2], people[i][2])

def small_board(board):
    l = len(board)
    print("------small board----")
    for i in range(l):
        for j in range(l):
            print(board[i][j], end=" ")
        print()

def board_print(arg, board):
    global n, m, people
    new_board = deepcopy(board)
    print("====",arg, "====")

    for i in range(m):
        if people[i][2] == 1:
            continue
        new_board[people[i][0]][people[i][1]] = "*"

    new_board[exit[0]][exit[1]] = "$"

    for i in range(n):
        for j in range(n):
            print(new_board[i][j], end=" ")
        print()


def move_people():
    global move, people, exit_people
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(m):
        d = 0
        if people[i][2] == 1:
            continue
        min_dis = abs(people[i][0] - exit[0]) + abs(people[i][1] - exit[1])
        for d_idx, dir in enumerate(direction):
            nx = people[i][0] + dir[0]
            ny = people[i][1] + dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != 0:
                continue
            distance = abs(nx - exit[0]) + abs(ny - exit[1])
            if distance < min_dis:
                d = d_idx
                min_dis = distance

        if min_dis != abs(people[i][0] - exit[0]) + abs(people[i][1] - exit[1]):
            people[i][0] += direction[d][0]
            people[i][1] += direction[d][1]
            move += 1
            if people[i][0] == exit[0] and people[i][1] == exit[1]:
                people[i][2] = 1
                exit_people += 1

def check_square(start, end):
    global board, people
    isexit = False
    ispeople = False
    people_pos = [people[i][:2] if people[i][2] == 0 else [-1, -1] for i in range(m)]
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if [i, j] in people_pos:
                ispeople = True
            if [i, j] == exit:
                isexit = True

            if ispeople and isexit:
                return True

    if isexit and ispeople:
        return True
    else:
        return False
def rotate_board():
    global board, people, exit
    #먼저 가장 작은 정사각형을 찾는다.
    sq = [0, 0, n - 1] #가장 큰 정사각형. (0,0) 좌측 상단에서 한변길이에 -1한거
    find_square = False
    for k in range(1, n):
        if find_square == True:
            break
        for i in range(0, n-k):
            if find_square == True:
                break
            for j in range(0, n-k):
                check = check_square((i, j), (i + k, j + k))
                if check:
                    sq = [i, j, k]
                    find_square = True
                    break

    new_small_board = [[0] * (sq[2] + 1) for _ in range(sq[2] + 1)]

    for i in range(sq[0], sq[0] + sq[2] + 1):
        for j in range(sq[1], sq[1] + sq[2] + 1):
            elm = board[i][j]
            dx = i - sq[0]
            dy = j - sq[1]
            if elm > 0:
                elm -= 1

            rotate_x = dy
            rotate_y = sq[2] - dx
            new_small_board[rotate_x][rotate_y] = elm

    #다시 붙여녛기
    for i in range(sq[2] + 1):
        for j in range(sq[2] + 1):
            dx = i + sq[0]
            dy = j + sq[1]
            board[dx][dy] = new_small_board[i][j]

    for i in range(m):
        tx, ty = people[i][:2]
        if sq[0] <= tx and tx < (sq[0] + sq[2] + 1) and sq[1] <= ty and ty < (sq[1] + sq[2] + 1):
            tx -= sq[0]
            ty -= sq[1]
            nx, ny = ty, sq[2] - tx
            people[i][0], people[i][1] = nx + sq[0], ny + sq[1]

    ex, ey = exit
    ex -= sq[0]
    ey -= sq[1]
    nx, ny = ey, sq[2] - ex
    exit = [nx + sq[0], ny + sq[1]]

# people_print(people)
# board_print("init", board)
while time <= k and exit_people < m:
    # print(exit_people)
    move_people()
    # board_print("after move", board)
    if exit_people == m:
        break
    rotate_board()
    # people_print(people)
    # board_print(time, board)
    time += 1
    # print(move)

##### ANS ######
print(move)
print(exit[0] + 1, exit[1] + 1)