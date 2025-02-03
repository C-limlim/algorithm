# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        inc_ans = 1
        dec_ans = 1
        ans = []
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                dec_ans += 1
                ans.append(inc_ans)
                inc_ans = 1
            elif nums[i-1] == nums[i]:
                ans.extend([dec_ans, inc_ans])
                dec_ans = inc_ans = 1
            else:
                inc_ans += 1
                ans.append(dec_ans)
                dec_ans = 1
        ans.extend([dec_ans, inc_ans])
        return max(ans)
