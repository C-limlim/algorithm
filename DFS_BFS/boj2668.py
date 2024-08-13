n = int(input())
row = [0]
visited = [False] * (n+1)
cyc = []
ans = []
    
for _ in range(n):
    row.append(int(input()))
    
def dfs(index):
    visited[index] = True
    num = row[index]
    cycle.append(index)
    
    if visited[num]:
        if num in cycle:
            ans.extend(cycle[cycle.index(num):])
    else:
        dfs(num)
        
for i in range(1, n+1):
    if not visited[i]:
        cycle = []
        dfs(i)

        
print(len(ans))
ans.sort()
for elm in ans:
    print(elm)
    