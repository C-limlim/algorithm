# 유적지 5x5, 1~7

# 1. 탐사 진행
## 3x3 격자 선택하여 회전, 시계방향 90-180-270
## - 획득 가치 최대화하는 회전 > 각도가 가장 작은 회전 > 중심좌표의 열 작은 구간 > 행 작은 구간

# 2. 유물 획득
## 1차획득
## - 상하좌우 인접 3개일 경우 조각 개수만큼 가치 획득
## - 열 번호 작은 순, 행 번호 큰순으로 조각 채우기

## 연쇄획득
## - 조각이 3개 이상 연결되지 않을 때까지 반복
## - 3개 이상 연결될 경우 가치 획득
## - 조각이 사라지면 또 채우기

# 3. 탐사 반복
## k번의 실행, 각 턴마다 획득한 유물의 가치 총합 출력
## k턴을 진행하지 못해도 유물을 획득할 수없다면 모든 탐사 종료, 종료턴에 아무값도 출력하지 않음
from collections import deque
from copy import deepcopy
import numpy as np


def make_board():
    board = []
    for _ in range(5):
        board.append(list(map(int, input().strip().split(" "))))
    return board

def get_candidates():
    return list(map(int, input().strip().split(" ")))

def pos_in_board(i, j):
    if 0 <= i and i < 5 and 0 <= j and j < 5:
        return True
    else:
        return False

def find_adj_positions(board):
    # 해당 보드에 대해 인접한 인덱스들 리턴
    positions = []
    visited = [[False for _ in range(5)] for _ in range(5)]
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                num = board[i][j]
                visited[i][j] = True
                q = deque([[i, j]])
                dump_num_pos = []

                while q:
                    curr_pos = q.popleft()
                    dump_num_pos.append(curr_pos)
                    for dir in range(4):
                        nx = curr_pos[0] + dx[dir]
                        ny = curr_pos[1] + dy[dir]
                        if pos_in_board(nx, ny) and not visited[nx][ny] and board[nx][ny] == num:
                            visited[nx][ny] = True
                            q.append([nx, ny])

                if len(dump_num_pos) >= 3:
                    positions.extend(dump_num_pos)

    return positions

def rotate_board(board, pos, angle):
    subboard = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            subboard[i][j] = board[pos[0] - 1 + i][pos[1] - 1 + j]
    new_subboard = [[0 for _ in range(3)] for _ in range(3)]
    new_subboard[1][1] = board[pos[0]][pos[1]]
    start = 0
    end = 2
    if angle >= 90:
        for y in range(start, end + 1):
            offset = y - start
            # 오 <- 위
            new_subboard[y][end] = subboard[start][y]
            # 아 <- 오
            new_subboard[end][end - offset] = subboard[y][end]
            # 좌 <- 아
            new_subboard[end-offset][start] = subboard[end][end-offset]
            # 오 <- 좌
            new_subboard[start][y] = subboard[end-offset][start]

    if angle >= 180:
        subboard = deepcopy(new_subboard)
        for y in range(start, end + 1):
            offset = y - start
            # 오 <- 위
            new_subboard[y][end] = subboard[start][y]
            # 아 <- 오
            new_subboard[end][end - offset] = subboard[y][end]
            # 좌 <- 아
            new_subboard[end-offset][start] = subboard[end][end-offset]
            # 오 <- 좌
            new_subboard[start][y] = subboard[end-offset][start]
    if angle >= 270:
        subboard = deepcopy(new_subboard)
        for y in range(start, end + 1):
            offset = y - start
            # 오 <- 위
            new_subboard[y][end] = subboard[start][y]
            # 아 <- 오
            new_subboard[end][end - offset] = subboard[y][end]
            # 좌 <- 아
            new_subboard[end-offset][start] = subboard[end][end-offset]
            # 오 <- 좌
            new_subboard[start][y] = subboard[end-offset][start]

    new_board = deepcopy(board)
    for i in range(3):
        for j in range(3):
            new_board[pos[0] - 1 + i][pos[1] - 1 + j] = new_subboard[i][j]
    return new_board

def find_center_pos(board):
    # 3x3 격자 선택하여 회전, 시계방향 90-180-270
    # 획득 가치 최대화, 회전 최소, 중심좌표 열 작고, 행 작고
    max_center_pos = [-1, -1]
    rotate_angle = 360
    max_values = 0

    for j in range(1, 4):
        for i in range(1, 4):
            # 90도
            board_90 = rotate_board(board,[i, j], 90)
            values_of_90 = len(find_adj_positions(board_90))
            if max_values < values_of_90:
                max_values = len(find_adj_positions(board_90))
                max_center_pos = [i, j]
                rotate_angle = 90

    for j in range(1, 4):
        for i in range(1, 4):
            # 180도
            board_180 = rotate_board(board, [i, j], 180)
            values_of_180 = len(find_adj_positions(board_180))
            if max_values < values_of_180:
                max_values = len(find_adj_positions(board_180))
                max_center_pos = [i, j]
                rotate_angle = 180

    for j in range(1, 4):
        for i in range(1, 4):
            # 270도
            board_270 = rotate_board(board, [i, j], 270)
            if max_values < len(find_adj_positions(board_270)):
                max_values = len(find_adj_positions(board_270))
                max_center_pos = [i, j]
                rotate_angle = 270

    return [max_center_pos, rotate_angle]

def fill_numbers(board, adj_pos_list, candidates):
    adj_pos_list.sort(key=lambda x: (x[1], -x[0]))
    for adj_pos in adj_pos_list:
        value = candidates.pop(0)
        board[adj_pos[0]][adj_pos[1]] = value
    return board

##################
### main solve ###

k, m = map(int, input().strip().split(" "))
board = make_board()
candidates = get_candidates()

while k > 0:
    answer = 0
    # 탐사 진행
    # 유물 1차 획득
    center_pos, rotate_angle = find_center_pos(board)
    if center_pos == [-1, -1]:
        break #회전해도 찾을 수 없었다면 끝

    board = rotate_board(board, center_pos, rotate_angle)
    adj_pos_list = find_adj_positions(board)
    answer += len(adj_pos_list)
    # 유물 채우기
    board = fill_numbers(board, adj_pos_list, candidates)
    adj_pos_list = find_adj_positions(board)

    # 유물 반복 획득
    while len(adj_pos_list) > 0:
        answer += len(adj_pos_list)
        board = fill_numbers(board, adj_pos_list, candidates)
        adj_pos_list = find_adj_positions(board)

    # 획득한 총합 출력, 만약 총합이 0이라면 멈추기
    if answer == 0:
        break
    else:
        print(answer, end=" ")

    k = k-1