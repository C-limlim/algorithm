class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        marked = [0] * n

        for i in range(n):
            if s[i] in "0123456789":
                marked[i] = 1
                for j in range(i - 1, -1, -1):
                    if marked[j] == 0:
                        marked[j] = 1
                        break
        
        return "".join([s[x] if marked[x] == 0 else "" for x in range(n)])
