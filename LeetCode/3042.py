class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            if str2[:len(str1)] == str1 and str2[-len(str1):] == str1: #startwith, endwith 써도 됨
                return 1
            else:
                return 0

        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans += isPrefixAndSuffix(words[i], words[j]) 

        return ans
        
    
