#문제: 루돌프의 반란
#nxn (r,c), 좌상단 (1,1)
#게임 m턴, 한턴: 루돌프 한번 - 1~p 산타 순서대로 움직임, 기절/게임탈락산타는 x
#두칸사이의거리는 유클라디안거리로
#루돌프: 게임탈락안한 가장가까운산타를향해1칸돌진, 
#   가장 가까운 산타가 2명 이상이라면 r,c 순서대로 큰 산타기준
#   상하좌우 + 대각선 총 8방향, 우선순위가 높은 산타를 향해
#산타: 루돌프에게 가까워지는방향으로 이동, 
#   다른 산타있는칸 x
#   움직일수없으면 안움직임, 있더라도 루돌프와 가까워지지않는다면X
#   상-우-하-좌 우선순위 4방향으로 움직일 수 있음
#충돌: 산타와 루돌프가 같은칸
#   루돌프가 움직였을때: 산타 +C, 산타는 루돌프가 이동해온 방향으로 C만큼 이동
#   산타가 움직였을 떄: 산타+D, 산타는 산타가 이동해온 반대방향으로 d만큼 이동
#   게임판밖이라면 산타 탈락
#   밀려난 칸에 다른산타: 상호작용
#   산타는 충돌 후 기절, K번째 턴에 기절할경우 (K+2)부터 정상화
#상호작용: 산타와 산타
#   기존의 산타는 1칸 해당방향으로 밀려남. 그 옆에 산타가 있다면 연쇄적으로 1칸. 게임판밖이면 탈락
#게임종료: M번의 턴, P산타 모두 탈락하면 그 즉시 종류
#   매 턴 이후 아직 탈락안한산타는 +1
import sys

def print_array(title, arr):
    depth = len(arr)
    width = len(arr[0])
    
    print("===" + title+ "===")
    for i in range(depth):
        for j in range(width):
            print(arr[i][j], end =" ")
        print()
    print("=================")
    
def solve():
    #input
    #1,1부터 시작한다는 기준이므로 좌표 다 1 빼줌
    n, m, p, c, d = map(int, input().split(" "))
    ru_x, ru_y = map(int, input().split(" "))
    ru_pos = [ru_x-1, ru_y-1]
    santa_info = [[0, m] for _ in range(p)] #점수, 참여 가능한 가장 높은 턴 (탈락하면 -1)
    santa_pos = [[0, 0] for _ in range(p)]
    for _ in range(p):
        idx, x, y = map(int, input().split(" "))
        santa_pos[idx-1] = [x-1, y-1]
    #상-우-하-좌-대각선4
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
      
    def move_ru():
        #가장 가까운 산타 찾기
        #r, c 순으로 큰 산타로 이동
        
        target = [-1, -1, 5000, -1] #산타 x, y, dis, idx
        for i in range(p):
            if santa_info[i][1] == -1:
                continue
            
            dis = cal_dis(ru_pos, santa_pos[i][0], santa_pos[i][1])
            if dis < target[2]:
                target[0], target[1], target[2], target[3] = santa_pos[i][0], santa_pos[i][1], dis, i
            elif dis == target[2]:
                if santa_pos[i][0] > target[0] or (santa_pos[i][0] == target[0] and santa_pos[i][1] > target[1]):
                    target[0], target[1], target[2], target[3] = santa_pos[i][0], santa_pos[i][1], dis, i

        if target[0] == -1: #game over
            return 1
        
        #target 산타쪽으로 이동하기
        #얘의 dis가 만약 0일 경우 crash, 아니면 그냥 넘기기
        #방향은 어떻게 찾지?... 빼자!
        move_x = 0 if target[0] == ru_pos[0] else (target[0] - ru_pos[0]) // abs(target[0] - ru_pos[0])
        move_y = 0 if target[1] == ru_pos[1] else (target[1] - ru_pos[1]) // abs(target[1] - ru_pos[1])
        
        ru_pos[0] += move_x
        ru_pos[1] += move_y
        
        if ru_pos == santa_pos[target[3]]:
            crash(-1, target[3], (move_x, move_y), m)
                 
    def move_santa(idx, m):
        #산타가 무사히 움직이면 m-1넣어줌, 기절할시 m -2, 죽을시 -1
        
        #가장 가까운 위치 찾기. 1)산타있으면 안됨
        info = [-1, cal_dis(ru_pos, santa_pos[idx][0], santa_pos[idx][1]), (0, 0)] #온 방향,루돌프와의 거리, 이동한곳
       
        for i in range(4):
            nx = santa_pos[idx][0] + dir[i][0]
            ny = santa_pos[idx][1] + dir[i][1]
            if [nx, ny] in santa_pos: #산타가 있는 곳으로 가지 않음
                continue
            dis = cal_dis(ru_pos, nx, ny)
            if dis == 0:
                santa_pos[idx][0] = nx
                santa_pos[idx][1] = ny
                santa_info[idx][1] = m-1  
                crash(idx, -1, dir[i], m) 
                return 0 #이 산타의 턴은 끝남
            
            if dis < info[1]: #우선순위보장 (지금것보다 낮으면 바꿈, 같으면 원래거)
                info[0], info[1], info[2] = i, dis, (nx, ny)
        #이동할 곳이 있을 때  
        if info[0] != -1:
            santa_pos[idx][0] = info[2][0]
            santa_pos[idx][1] = info[2][1]
        
        #턴 끗
        santa_info[idx][1] = m-1      
    
    def crash(idx, crash_idx, dir, turn):
        #인자: idx가 이동해 crash_idx에 부딫침, 현재 턴, 방향
        #해야할일: 위치 이동, 기절, 게임아웃, 점수
        #세가지 경우: 루돌프가 움직여 산타가 부딫침 / 산타가 움직여 루돌프가 부딫침 / 산타가 튕겨져 산타와 부딫침
        if idx == -1: #첫번째케이스.
            # 산타 +C, 기절, 산타는 루돌프가 이동해온 방향으로 C만큼 이동
            santa_info[crash_idx][0] += c
            santa_info[crash_idx][1] = 0 if turn - 2 < 0 else turn - 2
            new_pos = [santa_pos[crash_idx][0] + c * dir[0], santa_pos[crash_idx][1] + c * dir[1]]
            
            #게임판 나가면 아웃
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= n:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                santa_info[crash_idx][1] = -1
                return 0
            
            #새 위치에 산타나 루돌프가 있으면 crash
            if (new_pos in santa_pos):
                new_crash_idx = santa_pos.index(new_pos)
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                crash(crash_idx, new_crash_idx, dir, turn)
                
            elif new_pos == ru_pos:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                crash(crash_idx, -1, dir, turn)          
            else:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]    
                
        elif crash_idx == -1: #두번째 케이스.
            # 산타가 움직였을 떄: 산타+D, 산타는 산타가 이동해온 반대방향으로 d만큼 이동
            santa_info[idx][0] += d
            santa_info[idx][1] = 0 if turn - 2 < 0 else turn - 2
            new_pos = [santa_pos[idx][0] - d * dir[0], santa_pos[idx][1] - d * dir[1]]
            
            #게임판 나가면 아웃
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= n:
                santa_pos[idx][0], santa_pos[idx][1] = new_pos[0], new_pos[1]
                santa_info[idx][1] = -1
                return 0
            
            #이동했는데 다른 산타있음
            if (new_pos in santa_pos):
                new_crash_idx = santa_pos.index(new_pos)
                santa_pos[idx][0], santa_pos[idx][1] = new_pos[0], new_pos[1]
                crash(idx, new_crash_idx, (-dir[0], -dir[1]), turn)
            
            else:
                santa_pos[idx][0], santa_pos[idx][1] = new_pos[0], new_pos[1]
            #루돌프와 부딫쳤으므로 움직였을때 또 부딫치지 않음
                
        else: #산타산타 상호작용
            #기존의 산타는 1칸 해당방향으로 밀려남. 그 옆에 산타가 있다면 연쇄적으로 1칸. 게임판밖이면 탈락 
            new_pos = [santa_pos[crash_idx][0] + dir[0], santa_pos[crash_idx][1] + dir[1]]
            
            #게임판 나가면 아웃
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= n:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                santa_info[crash_idx][1] = -1
                return 0
            
            
            #이동했는데 다른 산타있음
            if (new_pos in santa_pos):
                new_crash_idx = santa_pos.index(new_pos)
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                crash(crash_idx, new_crash_idx, dir, turn)
            
            #이동했는데 루돌프있음:
            elif new_pos == ru_pos:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                crash(crash_idx, -1, dir, turn)
            else:
                santa_pos[crash_idx][0], santa_pos[crash_idx][1] = new_pos[0], new_pos[1]
                     
    def cal_dis(ru, santax, santay):
        return (ru[0] - santax) ** 2 + (ru[1] - santay) ** 2
     
    #게임하기 
    while m:
        game_over = move_ru()
        if game_over:
            break
        #print(ru_pos)
        for i in range(p):
            #움직일수잇는 산타 체크
            if santa_info[i][1] == m:
                move_santa(i, m)
            # for x in range(n):
            #     for y in range(n):
            #         a = "0"
            #         if [x, y] in santa_pos:
            #             a = santa_pos.index([x, y]) + 1
            #         if [x, y] == ru_pos:
            #             a = "-1"
            #         print(a, end=" ")
            #     print()
            # print("=============")
        m -=1     
           
        #살아남은산타에게 1
        for i in range(p):
            if santa_info[i][1] != -1:
                santa_info[i][0] += 1

                
        
    #결과출력
    for santa in santa_info:
        print(santa[0], end=" ")

   
solve()