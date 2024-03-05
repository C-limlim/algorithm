import sys 
sys.setrecursionlimit(100000)

def solve():
    n = int(input())
    graph = list(map(int, input().split(" ")))
    graph = [x - 1 for x in graph]
    visited = [False] * n

    #핵심은 다시 돌아와야함 ... cycle
    #처음 시작한게 마지막 갔을 때 같으면 되는거 아닌감??
    #아니었음... 1 -> 3 -> 5 -> 3 이면 3-5만 사이클임
    count = 0
    
    def dfs(idx):
        if visited[idx]: #이미 방문했는데
            if idx in cycle: #사이클에 있다면
                return len(cycle[cycle.index(idx):])
            else:
                return 0
        
        visited[idx] = True
        cycle.append(idx)
        return dfs(graph[idx])
        
    for i in range(n):               
        if not visited[i]:
            cycle = []
            count += dfs(i)
    
    print(n - count)
        
  
def problem():
    t = int(input())
    for _ in range(t):
        solve()
    
problem()