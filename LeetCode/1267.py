class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_servers = [0] * m
        col_servers = [0] * n

        for i in range(m):
            row_servers[i] = grid[i].count(1)
        
        for j in range(n):
            col_servers[j] = [grid[i][j] for i in range(m)].count(1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_servers[i] > 1 or col_servers[j] > 1:
                        ans += 1

        return ans
