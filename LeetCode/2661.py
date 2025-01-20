class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        # 오늘도 지피티와 함께...
        # 행열을 모두 채운다 == 가장 늦개등장하는 애 기준으로 빙고가 된다 == 그 행열에서 가장 늦은 인덱스가 채워지는 순서다 == max 중에서 min이 정답
        
        m, n = len(mat), len(mat[0])

        valtoidx = {arr[i]: i for i in range(m*n)}

        ans = m * n
        for row in mat:
            ans = min(ans, max([valtoidx[val] for val in row]))
        
        for col_idx in range(n):
            col = [mat[i][col_idx] for i in range(m)]
            ans = min(ans, max([valtoidx[val] for val in col]))

        return ans
