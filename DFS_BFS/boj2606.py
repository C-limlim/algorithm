def solve():
    print
    vertex = int(input())
    edge = int(input())
    graph = [[] for _ in range(vertex)] ## 1부터 시작하게
    visited = [False] * vertex
    
    for _ in range(edge):
        x , y = map(int, input().split(" "))
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    
    def dfs(i):
        if visited[i]:
            return 0
        
        visited[i] = True
        for adj in graph[i]:
            dfs(adj)
        return 1
        
    dfs(0)
        
    count = 0
    
    for i in range(vertex):
        if visited[i]:
            count += 1
    
    print(count - 1) #자기는 뺌 #visited.count(True)로도 셀 수 있군
    
solve()