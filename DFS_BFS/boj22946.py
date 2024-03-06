from collections import deque

def solve():
    n, m, v = map(int, input().split(" "))
    v = v -1
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split(" "))
        if y-1 not in graph[x-1]:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
    
    for i in range(n):
        graph[i].sort()
        
    visited = [False] * n
    
    def dfs(idx):
        if visited[idx]:
            return 0
        visited[idx] = True
        print(idx + 1, end=" ")
        for adj in graph[idx]:
            dfs(adj)   
    
    def bfs(idx):
        queue = deque()
        queue.append(idx)
        
        while queue:
            x = queue.popleft()
            if visited[x]:
                continue
            visited[x] = True
            print(x + 1, end=" ")
            
            for adj in graph[x]:
                queue.append(adj)
    
    dfs(v)
    print()
    visited = [False] * n
    bfs(v)

solve()