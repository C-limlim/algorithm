class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        w = " " + " ".join(words)
        return w.count(" "+pref)
