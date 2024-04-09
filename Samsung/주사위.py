#https://www.acmicpc.net/problem/23288
#(1,1) ~ (n,m)
#주사위 이동방향으로 한칸. 이동방향에 칸 없다면 이동방향 반대로 한칸
#위치의 점수 획득: 해당 칸의 정수 x 맞닿아있는 같은 정수 칸 개수
#방향결정: 주사위 아랫면 정수 - 주사위 칸 정수 비교해
#a>b 90도 시계 a<b 90도 반시계
from collections import deque


def cal_score(pos, board, direction):
    b = board[pos[0]][pos[1]]
    n = len(board)
    m = len(board[0])
    
    check = [[0] * m for i in range(n)]
    check[pos[0]][pos[1]] = 1
    #dfs나 bfs로 탐색
    q = deque([pos])
    count = 0
    while len(q) > 0:
        pos = q.popleft()
        count += 1
        
        for _, dir in enumerate(direction):
            new_pos = [pos[0] + dir[0], pos[1] + dir[1]]
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= m:
                continue
            else:
                if board[new_pos[0]][new_pos[1]] == b:
                    if not check[new_pos[0]][new_pos[1]]:
                        check[new_pos[0]][new_pos[1]] = 1
                        q.append(new_pos)              
    return b * count

class dice():
    def __init__(self):
        self.dir = 1 #방향 index
        self.row = [4, 1, 3, 6] # 0: 왼쪽 1: 정면위 2: 오른쪽 면 3.닿는면
        self.col = [2, 1, 5, 6] # 0: 옆쪽위 1:정면위 2: 아래 3:닿는면
        self.score = 0
        
    def print_dice(self):
        print("==========")
        print(" ", self.col[0])
        for i in range(3):
            print(self.row[i], end=" ")
        print()
        print(" ", self.col[2])
        print(" ", self.col[3])
        print("==========")
        
    def rotate(self, b):
        a = self.col[3]
        if a > b:
            self.dir = (self.dir + 1) % 4
        elif a < b:
            self.dir = (self.dir - 1 + 4) % 4
    
    def move(self, pos, direction, board):
        n = len(board)
        m = len(board[0])
        #1. 주사위 굴리기
        ## 새로운 포지션 찾기
        new_pos = [pos[0] + direction[self.dir][0], pos[1]+direction[self.dir][1]]
        if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= m:
            self.dir = (self.dir + 2) % 4
            new_pos = [pos[0] + direction[self.dir][0], pos[1]+direction[self.dir][1]]
        pos = new_pos
        
        ## 주사위 위치도 회전시키기
        if self.dir == 0: #위로 회전
            self.col = self.col[1:] + [self.col[0]]
            self.row[1] = self.col[1]
            self.row[3] = self.col[3]
                
        elif self.dir == 1: #동쪽 회전
            self.row = [self.row[3]] + self.row[:3]
            self.col[1] = self.row[1]
            self.col[3] = self.row[3]
        elif self.dir == 2: #남쪽 회전
            self.col = [self.col[3]] + self.col[:3]
            self.row[1] = self.col[1]
            self.row[3] = self.col[3]
        else: #서쪽 회전
            self.row = self.row[1:] + [self.row[0]]
            self.col[1] = self.row[1]
            self.col[3] = self.row[3]
        
        #2. 점수 획득
        self.score += cal_score(pos, board, direction)
        
        return pos
    
    def get_score(self):
        return self.score
    
def solve():
    #일차원배열은 새롭게 넘어가고 이차원배열은 shallow copy되고?
    n, m, k = map(int, input().split(" "))
    board = []
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북동남서 (시계방향)
    mydice = dice()
    pos = [0, 0]
    
    for _ in range(n):
        board.append(list(map(int, input().split(" "))))
        
    for _ in range(k):
        #print("=========")
        #주사위 이동 및 방향 결정, 점수 계산
        pos = mydice.move(pos, direction, board)
        
        #방향결정함수
        b = board[pos[0]][pos[1]]
        mydice.rotate(b)  
        
        #mydice.print_dice()
        #print(mydice.dir, mydice.score, pos)
        
    print(mydice.get_score())

solve()