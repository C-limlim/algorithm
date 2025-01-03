class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 길이 n, index i에서 valid split 가짐
        # i+1 element들의 합 >= n-i-1 element의 합
        # 최소 하나의 i가 존재하고, 0 <= i < n-1 임

        sum_list = [nums[0]]
        for i in range(1, len(nums)):
            sum_list.append(sum_list[-1] + nums[i])
            # i-1 하는 것보다 -1 하는게 속도가 훨씬 빠르네

        ans = 0
        for i in range(len(nums) -1):
            if sum_list[i] >= sum_list[-1] - sum_list[i]:
                ans += 1
        return ans
