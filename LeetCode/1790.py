#1790. Check if One String Swap Can Make Strings Equal

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        candidates = []

        for i in range(n):
            if s1[i] != s2[i]:
                candidates.append(i)
                
        if len(candidates) == 0:
            return True

        if len(candidates) != 2:
            return False
        else:
            if s1[candidates[0]] == s2[candidates[1]] and s1[candidates[1]] == s2[candidates[0]]:
                return True
            else:
                return False
