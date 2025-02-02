class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        x = 0
        for i in range(1, n):
            if nums[i-1] <= nums[i]:
                continue
            else:
                x = i
                break
        
        if x == 0:
            return True
        else:
            for i in range(x + 1, x + n):
                if nums[(i-1) % n] <= nums[i % n]:
                    continue
                else:
                    return False
            return True

    ## 포문 하나만 돌고도 할 수 있음
    ## num[i] > num[i+1] 이 두개 이상 있다면 rotate로 안되는것
