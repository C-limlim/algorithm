#문제: 게임개발
# nxm, 각 칸은 육지/바다, 캐릭터 동서남북 중 하나 바라봄
# 1. 현재 방향 기준 왼쪽방향부터 차례대로 갈 곳을 정함
# 2. 왼쪽방향에 아지 가보지 않은 칸이 존재한다면, 회전한다음 그 칸으로 전진
# 3. 가본 칸이라면 회전만 수행하고 1번으로 이동
# 4. 네방향 모두 이미 가본 칸이거나 바다인경우, 바라보는 방향 유지한채 한칸 뒤로, 1단계로. 뒷칸이 바다일경우에 움직임 정지
# 캐릭터가 방문한 칸의 수를 출력

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def solve():
    count = 1
    n, m = map(int, input().split(" "))
    x, y, d = map(int, input().split(" "))
    board = []
    dir = [(-1,0), (0,1), (1, 0), (0,-1)]
    # dx = [-1, 0, 1, 0]
    # dy = [0, 1, 0, -1]
     
    for i in range(n):
        row = list(map(int, input().split(" ")))
        board.append(row)
        
    #check = [arr[:] for arr in board]
    board[x][y] = 1
    
    while(1):
        flag = 0
        for i in range(4):
            #왼쪽 방향으로 회전
            #아예 함수로 뺀 경우도 있음 - turn_left(d)
            d = ((d - 1) + 4) % 4
            new_d = dir[d]
            new_x = x + new_d[0]
            new_y = y + new_d[1]
            
            if board[new_x][new_y] == 0:
                x = new_x
                y = new_y
                board[x][y] = 1
                count += 1
                break
            
            if i == 3:
                flag = 1
                
        if flag == 1:
            if board[x - dir[d][0]][y - dir[d][1]] == 1:
                break
            else:
                x = x - dir[d][0]
                y = y - dir[d][1]
                
    print(count)
    
    
solve()