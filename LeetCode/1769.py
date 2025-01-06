class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answers = []

        ans = 0
        n = len(boxes)
        for i in range(n):
            for j in range(n):
                if i == j:
                    pass
                else:
                    if boxes[j] != '0':
                        ans += abs(i - j)
            answers.append(ans)
            ans = 0
            
        return answers
