#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# 구슬 n번, 벽돌 w x h - 0: 빈공간
#규칙 1. 구슬은 좌우만 움직일 수 있어 맨 위의 벽돌만 깨트릴 수 있음
#규칙 2. 벽돌은 숫자 1-9이며 구슬이 명중한 벽돌은 상하좌우로 벽돌숫자-1만큼 같이 제거
#규칙 3. 제거되는 범위 내에 있는 벽돌은 동시제거
#규칙 4. 빈 공간이 있을경우 벽돌은 밑으로 떨어짐
#최대한 많은 벽돌을 제거하고 남은 벽돌 수
#ㅋ.. 그리디인줄 알았는데 전혀 아니었다. 예시에 서있는 설명이 떡하니 그리디 반례인데도...

from collections import deque
from copy import deepcopy

def print_board(board, h, w):
    print("=======================")
    for i in range(h):
        for j in range(w):
            print(board[j][i], end=" ")
        print()
    print("=======================")

################################################
    
def posssible_plan(n, w, answer):
    '''
    가능한 순서 계산해주는 함수: 총 w ^ n개
    '''
    if len(answer) == 0:
        for i in range(w):
            answer.append([i])
        return posssible_plan(n-1, w, answer)
    
    if n == 0:
        return answer
    
    new_answer = deque()
    while len(answer) > 0:
        plan = answer.popleft()
        for i in range(w):
            new_answer.append(plan + [i])
    return posssible_plan(n-1, w, new_answer)

def remove_blank(board):
    '''
    board에서 block을 내려주는 함수
    '''
    for _, col in enumerate(board): #총 w개
        flag = False
        for i in range(len(col)):      
            if col[i] != 0:             
                flag = True      
            elif flag and col[i] == 0:
                del col[i]
                col.appendleft(0)

def play_game(plan, board):
    '''
    plan 순서에 따라 블록을 없앤다.
    '''
    w = len(board)
    h = len(board[0])
    
    crash_block = deque()
    for _, col in enumerate(plan):
        
        #col에 가장 첫번째 block을 찾고 queue에 넣는다. 만약 없다면 큐에 안넣고 패스
        zero_num = board[col].count(0)
        if zero_num == h: #다 0이라면
            continue
        else:
            #만약 0이 하나도 없다면 0번째 idx부터 시작해야할것이고
            #만약 0이 두개라면 idx 2부터 시작해야한다.
            crash_block.append((zero_num, col))
        
        #연쇄작용으로 다 터트린다.
        while len(crash_block) > 0:
            #print(crash_block, crash_block[0])
            row, col = crash_block.popleft()
            crash_range = board[col][row]
            board[col][row] = 0
            
            #연쇄작용 처리 - range가 2 이상이면 걔네들의 여파들도 다 block에 넣어준다. 
            if crash_range > 1:
                for i in range(1, crash_range):
                    up_row = row - i
                    down_row = row + i
                    left_col = col - i
                    right_col = col + i
                    
                    if up_row >= 0:
                        if board[col][up_row] == 1:
                            board[col][up_row] = 0
                            
                        elif board[col][up_row] > 1:
                            crash_block.append((up_row, col))
                        
                    if down_row < h:
                        if board[col][down_row] == 1:
                            board[col][down_row] = 0
                            
                        elif board[col][down_row] > 1:
                            crash_block.append((down_row, col))
                        
                    if left_col >= 0:
                        if board[left_col][row] == 1:
                            board[left_col][row] = 0
                            
                        elif board[left_col][row] > 1:
                            crash_block.append((row, left_col))
                        
                    if right_col < w:
                        if board[right_col][row] == 1:
                            board[right_col][row] = 0
                            
                        elif board[right_col][row] > 1:
                            crash_block.append((row, right_col))
        remove_blank(board)
        #print_board(board, h, w)   
        
    num_of_remain_block = w * h
    for i in range(w):
        num_of_remain_block -= board[i].count(0)
                        
    return num_of_remain_block, board

def solve(test_case):
    n, w, h = map(int, input().split(" "))
    #col과 row가 뒤집힌거라 보면됨 
    #[{첫번쨰 col} {두번쨰 col} .... ]
    board = [deque() for _ in range(w)]
    check = True
    
    for i in range(h):
        row = list(map(int, input().strip().split(" ")))
        for j in range(w):
            board[j].append(row[j])
            if check and row[j] < 2:
                check = False
    
    if check:
        print("#"+str(test_case), 0)
        return 0
    
    #모든 경우의 수에 대해 해봐야함
    plans = posssible_plan(n, w, deque())
    answer, _ = play_game(plans.popleft(), deepcopy(board))
    
    while len(plans) > 0:
        curr_plan = plans.popleft()
        remained_block_num, _ = play_game(curr_plan, deepcopy(board))
        if remained_block_num < answer:
            answer = remained_block_num
    
    print("#"+str(test_case), answer)


#############################
for test_case in range(1, 1+int(input())):
    solve(test_case)