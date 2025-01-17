class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        # 힌트 보고 품
        # original의 모든 원소가 두번씩 등장함 
        # -> derived의 xor sum은 0이어야함 
        ans = 0
        for i in range(len(derived)):
            ans = ans ^ derived[i]
        return not ans
