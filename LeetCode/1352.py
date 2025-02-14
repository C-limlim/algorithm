class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]
        # 워크로드를 미리 알고 관련 메타데이터를 저장해두는게 정말 중요하구나
        # prefix(sum)은 단순하게 저장하고 그걸 활용해서 (e.g. 수식) 등으로 문제 조건 맞추기

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.prefix) <= k:
            return 0

        return self.prefix[-1] // self.prefix[-(k+1)]
