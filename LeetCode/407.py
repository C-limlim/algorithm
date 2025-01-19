import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # 잘 모르겠어서 지피티와 함께...
        # 가장자리의 높이가 중요 -> 이거보다 낮으면 물이 고임
        # 가장자리에서 bfs하기
        # 1번 예시를 보면, 주변 가장자리 중에서 가장 높이가 낮은 가장자리 - 현재 자리의 차이만큼 물이 참
        # 따라서 딴놈이랑 bfs해서 비교하기 전에, 최소값이랑 먼저 비교하려면 min heap 필요함
        # max(height, 현재 위치)로 물이 (차게된다면) 찬 높이로 갱신해둠
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        h = []
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j ==0 or j == n-1:
                    heapq.heappush(h, (heightMap[i][j], i, j))
                    visited[i][j] = True

        ans = 0

        while h:
            height, x, y = heapq.heappop(h)

            for dx, dy in d:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, height - heightMap[nx][ny])
                    heapq.heappush(h, (max(height, heightMap[nx][ny]), nx, ny))
        
        return ans
