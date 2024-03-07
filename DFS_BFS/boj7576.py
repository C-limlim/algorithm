#문제: 토마토
#mxn 상자, 하루 지나면 익은 토마토(1)의 인접한 곳에 있는 토마토는 익음
#상자 안 토마토가 모두 익는 최소 일수
#일부 칸에는 토마토가 들어있지 않을 수도 있음(-1)

#해결방법: 주변을 전파시킬 수 있는 토마토만 넣기
#그렇게해서 queue가 비었는데 0이 있으면 노 출력
from collections import deque

def solve():
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    m, n = map(int, input().split(" "))
    graph = []
    
    for i in range(n):
        row = list(map(int, input().split(" ")))
        graph.append(row)
        
    def bfs():
        queue = deque()
        already_finished = True
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    queue.append((i, j, 0))
                elif graph[i][j] == 0:
                    already_finished = False
                    
        if already_finished:
            return 0       
                    
        while queue:
            x, y, day = queue.popleft()
            day += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = day
                    queue.append((nx, ny, day))  
        return 1
    
    def check_toma():
        ans = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    return -1
                else:
                    if graph[i][j] > ans:
                        ans = graph[i][j]
        return ans
    
            
    finished = bfs()
    if finished:
        print(check_toma())
    else: #bfs를 돌리지 않음
        print(0)
    
solve()