#https://www.acmicpc.net/problem/20055
#벨트가 각 칸위의 로봇과 함께 한칸 회전한다.
#가장먼저 벨트에 올라간 로봇부터 벨트 회전방향으로 한칸 이동할 수 있으면 이동한다.
#   이동하려는 칸에 로봇 없고 && 내구도 1 이상이어야 한다
#올리는 위치의 칸의 내구도가 0이 아니라면 로봇을 올린다
#내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 
from collections import deque

def print_belt(belt, n):
    for i in range(n):
        print(belt[i], end=" ")
    print()
    for i in range(n, 2*n):
        print(belt[i], end=" ")
    print()

def solve():
    n, k = map(int, input().split(" "))
    durability = deque(list(map(int, input().split(" ")))) #내구도
    belt = deque([0] * (2 * n)) #로봇 여부
        
    turn = 0
    
    while True:
        if durability.count(0) >= k:
            break
        
        #1. 벨트 회전
        durability.rotate(1)
        belt.rotate(1)
        
        ## 로봇을 내린다.
        belt[n-1] = 0
        
        #2. 오른쪽부터 로봇 한칸씩 옮기기
        for i in range(n-2, 0, -1):
            if belt[i] == 1: #현재칸에 로봇이 있다면
                #오른쪽이 비어있고 내구도가 남아있다면
                if belt[i+1] == 0 and durability[i+1] > 0:
                    #로봇을 옮겨주고 내구도 감소시킨다.
                    belt[i+1], belt[i] = 1, 0
                    durability[i+1] -= 1
                    
        ## 로봇을 한번더 내려준다.
        belt[n-1] = 0
        
        #3. 로봇 올리기
        if belt[0] == 0 and durability[0] > 0:
            belt[0] = 1
            durability[0] -= 1
        
        # print_belt(belt, n)
        # print_belt(durability, n)
        # print("======", turn + 1, "======")
        turn += 1
        
    print(turn)
solve()
