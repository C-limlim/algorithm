class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = set()

        for word in words:
            for comp_word in words:
                if word == comp_word: #모든 단어 unique
                    continue
                if word in comp_word:
                    ans.add(word)
                    continue
        
        return list(ans)
    
    # 대박코드
    # a = " ".join(words)
    # return [w for w in words if a.count(w) > 1]
