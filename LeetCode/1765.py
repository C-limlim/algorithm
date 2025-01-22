from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        ans = [[-1] * n for _ in range(m)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    ans[i][j] = 0
       
        # 헷갈렸던 점: 물마다 bfs를 해야한다고 생각했는데 그럼 기대값보다 높은 값으로 저장됨
        # 동시에 확산하는 것처럼 해야함 -> 큐에 물 위치 넣어놓고 그것부터 bfs해서 그 셀에 도착하는
        # 가장 빠른 height를 저장할 것
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))
        
        return ans
