from collections import deque
from copy import deepcopy

l, n, q = map(int, input().strip().split(" "))
board = []
knight_board = [["*"] * l for _ in range(l)]
knight = [] #위치x, y, 방패h, w, k, 게임아웃여부
knight_life = []
king = []
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] #위, 오, 아, 왼

for _ in range(l):
    board.append(list(map(int, input().strip().split(" "))))

for _ in range(n):
    tmp = list(map(int, input().strip().split(" ")))
    for i, pos in enumerate(tmp[:2]):
        tmp[i] = pos - 1
    knight.append(tmp + [0])
    knight_life.append(tmp[4])

for _ in range(q):
    tmp = list(map(int, input().strip().split(" ")))
    tmp[0] -= 1
    king.append(tmp)
def board_print(board):
    line = len(board)
    print("==============")
    for i in range(line):
        for j in range(line):
            print(board[i][j], end=" ")
        print()
def create_knight_board():
    global knight_board, knight
    new_knight_board = [["*"] * l for _ in range(l)]
    for idx, k in enumerate(knight):
        if k[5] == 1: #게임아웃
            continue
        start = (k[0], k[1])
        end = (start[0] + k[2], start[1] + k[3])
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                new_knight_board[i][j] = idx

    knight_board = deepcopy(new_knight_board)
def move_knight(command):
    k = command[0] #기사 인덱스
    d = command[1] #방향
    moved_knight = []
    q = deque([k])
    can_move = True
    while len(q):
        k = q.popleft()
        #이 기사의 새로운 위치를 계산한다.
        start = (knight[k][0] + dir[d][0], knight[k][1] + dir[d][1])
        end = (start[0] + knight[k][2], start[1] + knight[k][3])

        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                if i < 0 or i >= l or j < 0 or j >= l: #밖으로나간다면 아웃
                    can_move = False
                    return 0

                if board[i][j] == 2:
                    can_move = False
                    return 0

                if knight_board[i][j] != "*": #기사가 있다면
                    if knight_board[i][j] in moved_knight or knight_board[i][j] == command[0]:
                        continue
                    moved_knight.append(knight_board[i][j])
                    q.append(knight_board[i][j])

    if can_move:
        #첫번째 기사 위치 이동
        k = command[0]
        knight[k][0] += dir[d][0]
        knight[k][1] += dir[d][1]

        #나머지 이동한 기사 위치 이동
        for i, k in enumerate(moved_knight):
            knight[k][0] += dir[d][0]
            knight[k][1] += dir[d][1]

    return moved_knight

def check_damage(moved_knight):
    global knight
    damaged = 0
    for _, k_idx in enumerate(moved_knight):
        k = knight[k_idx]
        start = (k[0], k[1])
        end = (start[0] + k[2], start[1] + k[3])
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                if board[i][j] == 1:
                    damaged += 1

        knight[k_idx][4] -= damaged
        if knight[k_idx][4] <= 0:
            knight[k_idx][5] = 1
        damaged = 0

#첫번쨰 한번 생성
create_knight_board()

#command 실행
for _, command in enumerate(king):
    if knight[command[0]][5] == 1:
        continue
    moved_knight = move_knight(command)
    if moved_knight != 0:
        check_damage(moved_knight)
    create_knight_board()

#계산
ans = 0
for idx, k in enumerate(knight):
    if k[5] == 1:
        continue
    ans += knight_life[idx] - k[4]

print(ans)
