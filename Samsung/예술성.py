from copy import deepcopy
from collections import deque
n = int(input())
board = []
ans = 0
def board_print(board):
    l = len(board)
    print("++++++++++++++++++")
    for i in range(l):
        for j in range(l):
            print(board[i][j], end=" ")
        print()


for _ in range(n):
    board.append(list(map(int, input().strip().split(" "))))

def get_score():
    global board, n

    #group_board에 그룹 정보 저장
    group_board = [[0] * n for _ in range(n)]
    group = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(n):
            if group_board[i][j] > 0:
                continue
            group += 1
            q = deque([(i, j)])
            while len(q) != 0:
                pos = q.popleft()
                curr_num = board[pos[0]][pos[1]]
                group_board[i][j] = group
                for _, dir in enumerate(direction):
                    dx = pos[0] + dir[0]
                    dy = pos[1] + dir[1]
                    if dx < 0 or dx >= n or dy < 0 or dy >= n:
                        continue
                    if group_board[dx][dy] == 0 and board[dx][dy] == curr_num:
                        group_board[dx][dy] = group
                        q.append((dx, dy))

    #점수계산
    ##먼저 각 group의 개수를 알려줄 list 선언, 변의 개수 담을 list 선언
    ##변의개수는 더 작은 group number 수로 계산한다.
    ##생각해보니 절반만 돌려도 될지도..? 하지만 그냥 간다.
    num_of_group_list = [0] * (group+1)
    group_val_list = [0] * (group + 1)
    line_of_group_comb_list = [[0] * (group+1) for _ in range((group+1))]

    for i in range(n):
        for j in range(n):
            group_num = group_board[i][j]
            num_of_group_list[group_num] += 1
            group_val_list[group_num] = board[i][j]
            for _, dir in enumerate(direction):
                dx = i + dir[0]
                dy = j + dir[1]
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    continue
                adj_group_num = group_board[dx][dy]
                if group_num == adj_group_num:
                    continue
                line_of_group_comb_list[group_num][adj_group_num] += 1

    sum_group_score = 0
    for i in range(1, group + 1):
        for j in range(1, group + 1):
            if j < i:
                sum_group_score += (num_of_group_list[i] + num_of_group_list[j]) \
                                   * group_val_list[i] * group_val_list[j] * line_of_group_comb_list[i][j]

    return sum_group_score

def rotate_board():
    global board
    new_board = deepcopy(board)
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    center_pos = n // 2

    #십자모양
    for i in range(1, n // 2 + 1):
        for j, dir in enumerate(direction):
            dx = center_pos + dir[0] * i
            dy = center_pos + dir[1] * i
            curr_num = board[dx][dy]
            next_dir = j + 1 if j + 1 < 4 else 0
            new_dx = center_pos + direction[next_dir][0] * i
            new_dy = center_pos + direction[next_dir][1] * i
            new_board[new_dx][new_dy] = curr_num

    #정사각형 (n x n 크기의 회전이라고 생각해야함..)
    for i in range(center_pos):
        new_col = center_pos - 1 - i
        for j in range(center_pos):
            new_board[j][new_col] = board[i][j]

    #좌측 하단
    for i in range(center_pos + 1, n):
        new_col = center_pos - 1 - i + (center_pos + 1)
        for j in range(center_pos):
            new_row = j + center_pos + 1
            new_board[new_row][new_col] = board[i][j]

    #우측 상단
    for i in range(center_pos):
        new_col = n - 1 - i
        for j in range(center_pos + 1, n):
            new_row = j - (center_pos + 1)
            new_board[new_row][new_col] = board[i][j]
    #
    for i in range(center_pos + 1, n):
        new_col = center_pos + 1 + n - 1 - i
        for j in range(center_pos + 1, n):
            new_board[j][new_col] = board[i][j]

    board = deepcopy(new_board)




#init score
ans += get_score()
rotate_board()
for _ in range(3):
    ans += get_score()
    rotate_board()
print(ans)
