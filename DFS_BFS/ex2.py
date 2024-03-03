#문제: 미로 탈출
#NxM 미로, (1,1)시작, 출구 (N,M), 괴물 없는 부분 1, 탈출을 위한 최소 칸의 개수
#시작칸과 마지막 칸 모두 포함
#해결방법: bfs
#왜냐하면 가까운곳부터 탐색해나가며 탈출해야하기 때문... 깊게 갔다가 다시 돌아오면 시간낭비
#그러면 cycle찾는 문제는 dfs가 나은건가?
#근데 어떻게 최소칸을 쓰지? 따로 리스트를 만들어? 걸린 개수를? 
#bfs는 queue지 재귀가 아닌데 자꾸 재귀를 쓰려고하네 내가. 더 많은 수련이 필요하다

from collections import deque

def solve():
    n, m = map(int, input().split(" "))
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


    def bfs(x, y):
        # bfs는 큐가 빌때까지
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            # 괴물이 있는 곳은 가면 안됨
            if graph[x][y] == 0:
                return 0
        
            # 이제 주변 방문을 해... 그다음에 어떻게 해?
            # (해설 참고) 방문 안했을 때 step을 찍어! 그리고 queue에 넣어!
            # 궁금증: 어차피 아래로 내려가는게 최단거리라면 꼭 상하좌우 다 해줘야하나?_?
            # 당연... 왜냐하면 미로라는게 아래로 내려갔다 위로 올라가야하는 하나의 길이 있을수 있으니까!!!
            for i in range(4):
                nx = x + dir[i][0]
                ny = y + dir[i][1]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue  
                  
                if graph[nx][ny] == 1:               
                    graph[nx][ny] = graph[x][y] + 1  
                    queue.append((nx, ny))
    
    bfs(0, 0)
    
    print(graph[n-1][m-1])
    
solve()