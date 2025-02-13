class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)

        x = heapq.heappop(nums)
        ans = 0

        while k > x:
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            ans += 1

            x = heapq.heappop(nums)
            
        return ans
