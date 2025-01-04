class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 지피티랑 같이 풀음...
        # 모범답안: (리트코드 풀이 참고)
        # set(s) 로 하고, 이 set안의 문자열에 대해서
        # find와 rfind로 문자열 좌우 인덱스 찾고
        # len(set[left:right+1])를 리턴하면 됨 -> set를 하면 겹치는거 사라져서

        positions = {ch: [] for ch in "abcdㅁefghijklmnopqrstuvwxyz"}
        for i, ch in enumerate(s):
            positions[ch].append(i)

        unique_palindromes = set()

        for ch in positions:
            if len(positions[ch]) < 2: 
                continue
            left, right = positions[ch][0], positions[ch][-1]
            
            for mid in set(s[left + 1:right]):
                unique_palindromes.add((ch, mid, ch))

        return len(unique_palindromes)
