class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tmp = ans = nums[0]

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                tmp += nums[i]
            else:
                ans = max(ans, tmp)
                tmp = nums[i]
        return max(ans, tmp)
