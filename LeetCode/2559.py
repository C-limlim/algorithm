class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        isvowel = []
        vowel = ["a", "e", "i", "o", "u"]

        # 아래 두개의 반복문을 하나로 합칠 수 있음 !
        # e.g. for word in words:
        #          dp[i] = dp[i-1] + word[0] in vowels and word[-1] in vowels
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                isvowel.append(1)
            else:
                isvowel.append(0)
        
        for i in range(1, len(isvowel)):
            isvowel[i] += isvowel[i-1]

        for l, r in queries:
            if l == 0:
                ans.append(isvowel[r])
            else:
                ans.append(isvowel[r] - isvowel[l-1])
        
        return ans
