class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        for i in range(1, n):
            top_prefix[i] = top_prefix[i-1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i-1] + grid[1][i]
        
        result = float('inf')

        for i in range(n):
            # i열에서 첫번째 로봇 내려갔을 때 남은 점수는
            top_point = top_prefix[-1] - top_prefix[i]
            bottom_point = bottom_prefix[i - 1] if i > 0 else 0
            
            # 0 0 0 1 2  <- 첫번쨰 로봇이 지나간 이후 두번쨰 로봇의 선택은 세가지로 나눌 수 있다. 1) 1번 경로 따라가기 2)1번 경로보다 더 빨리 내려가기 3) 1번 경로보다 늦게 내려가기
            # 1 1 0 0 0     1) 바보같은 선택 2) 최대한 빨리 내려가야 함 == bottom_point 획득 3) 맨 끝에서 내려가야 함 == top_point 획득
            # 따라서 두번째 로봇이 가질 수 있는 최대 포인트는 max(top, bottom)
            second_robot_point = max(top_point, bottom_point)
            
            #첫번째 로봇은 두번째 로봇의 점수를 최소화 하는 경로를 선택한다
            result = min(second_robot_point, result)
        
        return result
        
