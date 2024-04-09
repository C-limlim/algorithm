#나무 성장
#1. 특수영양제 이동
#2. 땅에 영양제 투입 후 삭제 + 나무 1 증가됨
#3. 영양제 투입 땅에 있는 나무는 대각선 인접방향에 크기 1이상의 나무가 있는 만큼 높이 성장
#4. 영양제 안받은 나무 제외하고 높이 2이상 나무는 높이 2를 베어서 현재 위치에 영양제 구매
#년도별 규칙이 주어질 떄 최종 나무늬 높이들의 총합
def print_arr(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print("+++++++++++")

n, m = map(int, input().split(" "))
tree_board = []
rules = []
for _ in range(n):
    tree_board.append(list(map(int, input().split(" "))))
for _ in range(m):
    rules.append(list(map(int, input().split(" "))))

med_pos = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

#idx그대로쓰기위해서 앞에 하나 넣어줌
direction = [(0,0), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

def move_med(rule):
    global med_pos, direction
    new_med_pos = []
    for _, pos in enumerate(med_pos):
        #대각선 넘어가는걸 처리해준다. #(이동방향, 이동칸수)
        dx = (pos[0] + rule[1] * direction[rule[0]][0] + n) % n
        dy = (pos[1] + rule[1] * direction[rule[0]][1] + n) % n
        new_med_pos.append((dx, dy))

    med_pos = new_med_pos

def use_med():
    global tree_board, med_pos
    diagonal = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    #영양제 투입으로 나무 +1
    for _, pos in enumerate(med_pos):
        tree_board[pos[0]][pos[1]] += 1

    #대각선 위치에 있는 모든 tree가 1 이상이면 + 1 해준다.
    for _, pos in enumerate(med_pos):
        for _, dia in enumerate(diagonal):
            dx = pos[0] + dia[0]
            dy = pos[1] + dia[1]

            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue

            if tree_board[dx][dy] > 0:
                tree_board[pos[0]][pos[1]] += 1


def buy_med():
    global med_pos
    new_med_pos = []
    for i in range(n):
        for j in range(n):
            #영양제 있었던 자리는 살 수 없다
            if (i, j) in med_pos:
                continue

            if tree_board[i][j] >= 2:
                tree_board[i][j] -= 2
                new_med_pos.append((i, j))

    med_pos = new_med_pos

def sum_tree():
    global tree_board
    ans = 0
    for i in range(n):
        ans += sum(tree_board[i])
    return ans

for idx, rule in enumerate(rules):
    move_med(rule)
    use_med()
    buy_med()

ans = sum_tree()
print(ans)
