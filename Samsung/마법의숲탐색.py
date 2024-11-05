# R X C 배열 탐색, 1~R, 1~C
# 정령은 숲의 북쪽을 통해서만 들어올 수 있음
# k명의 정령이 각각 골렘을 타고 숲을 탐색
## 각 골렘은 십자 모양의 구조, 중앙칸 포함 5칸
## 중앙 제외 4칸 중 한칸은 골렘의 출구, 어떤 방향에서도 정령은 골렘 탑승이 가능하나 출구로만 내릴 수 있음
# i번째로 숲탐색하는 골렘은 가장북쪽에서 시작하여 중앙이 ci열이 되도록 하는 위치에서 내려옴, 초기 골렘의 출구는 di방향
# 더이상움직이지못할때까지 탐색, 탐색 선순위
## - 남쪽으로 한칸, 다 비어있어야 내려가기 가능
## - 서쪽으로(왼) 한칸 이동후 아래로 한칸, 반시계 회전
## - 동쪽으로(오) 한칸 이동후 아래로 한칸, 반시계 회전

# 골렘이 더이상 아래로 내려갈 수 없으면 정령은 골렘 내에서 상하좌우 인접 칸으로 이동 가능 (이때까지 정령은 가운데)
# - 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 갈 수 있음
# - 갈 수 있는 모든 칸 중 가장 남쪽의 칸으로 정령이 이동, 최종 위치가 됨

# 골렘이 다 내려갔는데 몸 전체가 숲 안에 들어와있지 않다면
## 숲 초기화, 다음골렘부터 새로 시작
## 정령 위치 누적합 구하기

from collections import deque
from copy import deepcopy

class Monster:
    def __init__(self, center_pos, exit_dir, order):
        self.center_pos = center_pos
        self.top_pos = [center_pos[0] - 1, center_pos[1]]
        self.right_pos = [center_pos[0], center_pos[1] + 1]
        self.left_pos = [center_pos[0], center_pos[1] - 1]
        self.down_pos = [center_pos[0] + 1, center_pos[1]]
        self.exit_dir = exit_dir
        self.order = order

    def get_all_pos(self):
        return [self.center_pos, self.left_pos, self.down_pos, self.right_pos, self.top_pos]

    def move_down(self):
        self.center_pos[0] += 1
        self.top_pos[0] += 1
        self.right_pos[0] += 1
        self.left_pos[0] += 1
        self.down_pos[0] += 1

    def move_right(self):
        self.center_pos = [self.center_pos[0] + 1, self.center_pos[1] + 1]
        self.top_pos = [self.center_pos[0] - 1, self.center_pos[1]]
        self.right_pos = [self.center_pos[0], self.center_pos[1] + 1]
        self.left_pos = [self.center_pos[0], self.center_pos[1] - 1]
        self.down_pos = [self.center_pos[0] + 1, self.center_pos[1]]
        self.exit_dir = (self.exit_dir + 1) % 4

    def move_left(self):
        self.center_pos = [self.center_pos[0] + 1, self.center_pos[1] - 1]
        self.top_pos = [self.center_pos[0] - 1, self.center_pos[1]]
        self.right_pos = [self.center_pos[0], self.center_pos[1] + 1]
        self.left_pos = [self.center_pos[0], self.center_pos[1] - 1]
        self.down_pos = [self.center_pos[0] + 1, self.center_pos[1]]
        self.exit_dir = (self.exit_dir + 3) % 4

    def get_exit_pos(self):
        if self.exit_dir == 0:
            return self.top_pos
        elif self.exit_dir == 1:
            return self.right_pos
        elif self.exit_dir == 2:
            return self.down_pos
        else:
            return self.left_pos


def pos_in_board(i, j):
    return i <= r and 1 <= j and j <= c



def okay_to_move(monster, board, dir):
    monster_pos = monster.get_all_pos()
    for pos in monster_pos:
        if pos[0] < 1:
            continue
        if dir == "down":
            i = pos[0] + 1
            j = pos[1]
            if not pos_in_board(i, j) or board[i][j] != 0:
                return False
        elif dir == "left":
            i = pos[0]
            j = pos[1] - 1
            if not pos_in_board(i, j) or board[i][j] != 0:
                return False
        else:
            i = pos[0]
            j = pos[1] + 1
            if not pos_in_board(i, j) or board[i][j] != 0:
                return False
    return True


def move_monster(monster, board):
    '''
    input: monster, board
    return: 위치 바뀐 monster
    '''
    flag = True
    while flag:
        if okay_to_move(monster, board, "down"):
            flag = True
            monster.move_down()
        elif okay_to_move(monster, board, "left"):
            new_monster = Monster([monster.center_pos[0], monster.center_pos[1] - 1], monster.exit_dir, monster.order)
            if okay_to_move(new_monster, board, "down"):
                flag = True
                monster.move_left()
            else:
                flag = False
        elif okay_to_move(monster, board, "right"):
            new_monster = Monster([monster.center_pos[0], monster.center_pos[1] + 1], monster.exit_dir, monster.order)
            if okay_to_move(new_monster, board, "down"):
                flag = True
                monster.move_right()
            else:
                flag = False
        else:
            flag = False

    return monster

def monster_in_board(monster, board):
    for pos in monster.get_all_pos():
        if pos[0] < 1 or pos[0] > r + 1 or pos[1] < 1 or pos[1] > c + 1:
            return False
    return True

def save_monster_in_board(monster, board, order):
    exit_pos = monster.get_exit_pos()
    for pos in monster.get_all_pos():
        if pos == exit_pos:
            board[pos[0]][pos[1]] = -order
        else:
            board[pos[0]][pos[1]] = order
    return board

def find_fairy_pos(monster, board):
    fairy_pos = monster.center_pos
    visited = deepcopy(board)
    q = deque([[fairy_pos, monster.order]])
    visited[fairy_pos[0]][fairy_pos[1]] = '$'

    while q:
        curr_pos, mon_order = q.popleft()
        if fairy_pos[0] < curr_pos[0]:
            fairy_pos = curr_pos
        for dir in [[-1, 0], [0, 1], [1, 0], [0, -1]]: #위오아좌
            nx = curr_pos[0] + dir[0]
            ny = curr_pos[1] + dir[1]
            if not pos_in_board(nx, ny):
                continue
            if visited[nx][ny] != '$' and visited[nx][ny] != 0:
                if abs(visited[nx][ny]) == abs(mon_order):
                    q.append([[nx, ny], visited[nx][ny]])
                    visited[nx][ny] = '$'

                elif mon_order < 0:
                    # 움직이려는데가 다른 몬스터인데 내가 지금 잇는데가 출구일 때
                    q.append([[nx, ny], visited[nx][ny]])
                    visited[nx][ny] = '$'

    return fairy_pos

######################################
global r
global c
r, c, k = map(int, input().strip().split(" "))
monster_cmd = [[0,0]]
for _ in range(k):
    monster_cmd.append(list(map(int, input().strip().split(" ")))) # 출발하는 열, 출구방향 (0,1,2,3 북동남서)
#######################################
answer = 0
board = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
monsters_in_board = []

for order in range(1, k+1):
    monster = Monster([-1, monster_cmd[order][0]], monster_cmd[order][1], order)
    # 1. 골렘 이동
    monster = move_monster(monster, board)

    # 2-1. 다 이동했는데 골렘이 숲 안에 못들어왔다면
    if not monster_in_board(monster, board):
        monsters_in_board = []
        board = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        continue

   # 2-2. 그렇지 않다면 board에 monster 박기 & monster 추가
    monsters_in_board.append(monster)
    board = save_monster_in_board(monster, board, order)

    # 3. 정령 이동
    fairy_pos = find_fairy_pos(monster, board)

    # 4. answer에 정령 좌표 더하기
    answer += fairy_pos[0]


print(answer)
