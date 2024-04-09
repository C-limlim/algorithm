from copy import deepcopy
n, m, k, c = map(int, input().strip().split(" "))
tree_board = []
for _ in range(n):
    tree_board.append(list(map(int, input().strip().split(" "))))

killer_board = [[0] * n for _ in range(n)]
ans = 0

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print("=================")

def grow_tree():
    global tree_board, n
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상, 하, 좌, 우
    new_tree_board = deepcopy(tree_board)

    for i in range(n):
        for j in range(n):
            count = 0
            if tree_board[i][j] <= 0:
                continue
            #주변 4개 중 tree가 있는 칸의 개수를 계산한다
            for _, dir in enumerate(direction):
                dx = i + dir[0]
                dy = j + dir[1]
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    continue
                if tree_board[dx][dy] > 0:
                    count += 1

            new_tree_board[i][j] += count

    tree_board = deepcopy(new_tree_board)
    # print("grow tree")
    # print_board(tree_board)

def spread_tree():
    global tree_board, n
    diag = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_tree_board = deepcopy(tree_board)

    for i in range(n):
        for j in range(n):
            count = []
            if tree_board[i][j] == -1:
                continue
            for _, dia in enumerate(diag):
                dx = i + dia[0]
                dy = j + dia[1]
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    continue
                if tree_board[dx][dy] == 0 and killer_board[dx][dy] == 0:
                    count.append((dx, dy))
            if len(count) != 0:
                add_tree = tree_board[i][j] // len(count)
                for _, spread_pos in enumerate(count):
                    new_tree_board[spread_pos[0]][spread_pos[1]] += add_tree

    tree_board = deepcopy(new_tree_board)
    # print("spread")
    # print_board(tree_board)

def find_kill_pos():
    global tree_board, k
    new_tree_board = deepcopy(tree_board)
    diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    #모든 block에 대해서 박멸되는 나무 수를 새준다.
    for i in range(n):
        for j in range(n):
            if tree_board[i][j] <= 0:
                continue
            for _, dia in enumerate(diag):
                for kk in range(1, k+1):
                    dx = i + kk * dia[0]
                    dy = j + kk * dia[1]
                    if dx < 0 or dx >= n or dy < 0 or dy >= n:
                        continue
                    if tree_board[dx][dy] <= 0:
                        break
                    else:
                        new_tree_board[i][j] += tree_board[dx][dy]

    killed_tree = 0
    ans_pos = [-1, -1]
    for i in range(n):
        for j in range(n):
            if killed_tree < new_tree_board[i][j]:
                killed_tree = new_tree_board[i][j]
                ans_pos[0], ans_pos[1] = i, j
    # print("find_best")
    # print_board(new_tree_board)
    return ans_pos

def kill_tree():
    global n, tree_board, ans
    #제일 효율적인 위치를 뽑는다
    kill_pos = find_kill_pos()
    if kill_pos == [-1, -1]:
        return True

    #살충제를 뿌린다.
    diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    #현재 위치에 뿌려준다
    ans += tree_board[kill_pos[0]][kill_pos[1]]
    tree_board[kill_pos[0]][kill_pos[1]] = 0
    killer_board[kill_pos[0]][kill_pos[1]] = c + 1

    #확산시켜준다
    for _, dia in enumerate(diag):
        for kk in range(1, k + 1):
            dx = kill_pos[0] + kk * dia[0]
            dy = kill_pos[1] + kk * dia[1]
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
            #제초제를 뿌리면 해당 위치의 tree는 사라지고 살충제는 c동안 남는다.
            #제거된 tree 수를 더해준다.
            if tree_board[dx][dy] <= 0: #만약 나무가 없거나 벽이면 여기서 그만한다
                killer_board[dx][dy] = c + 1
                break
            else:
                killer_board[dx][dy] = c + 1
                ans += tree_board[dx][dy]
                tree_board[dx][dy] = 0
    # print("kill")
    # print_board(tree_board)
    # print("killer")
    # print_board(killer_board)
    return False

def minus_kill():
    global killer_board, n
    for i in range(n):
        for j in range(n):
            if killer_board[i][j] > 0:
                killer_board[i][j] -= 1

for i in range(m):
    grow_tree()
    spread_tree()
    game_over = kill_tree()
    if game_over:
        break
    minus_kill()

print(ans)