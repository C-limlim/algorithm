#문제: 음료수 얼려 먹기
#NxM, 아이스크림 개수 구하기
#해결방법: dfs
# 일단 방문 -> 상하좌우 탐색 -> 0 이고 visited 안했으면 거기로 이동
# 거기서 또 반복 -> 없을 때까지
# visited 안한 노드로 또 이동
# 여기서의 visited는 1로 바꿔주면됨 막혀있거나 방문했거나는 둘다 못가기 때문에

def solve():
    n, m = map(int, input().split(' '))
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))  
        
    def dfs(x, y):
        # 칸을 넘어가면 즉시 종료되게 만들기 (재귀에서 내가 잘 못쓰는거, 일단 뒤로 넘기고 걔네가 조건 확인하기)
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        
        if graph[x][y] == 1:
            return False
        
        graph[x][y] = 1
    
        #상하좌우
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1
    
    print(result)
    
solve()