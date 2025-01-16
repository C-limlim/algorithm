class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)

        #좋은 함수지만 실제 실행은 for문으로 직접 했을 때보다 느리다
        xor_num1 = reduce(lambda x, y: x^y, nums1)
        xor_num2 = reduce(lambda x, y: x^y, nums2)
        
        #xor은 같은거끼리 하면 0이다. (상쇄)
        #0과 xor하면 0이다.
        return (xor_num1 * (n % 2))^ (xor_num2 * (m % 2))
