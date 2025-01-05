class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        # 시간초과 난 방식, dp로 풀어야 함
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # moves = [0] * len(s)

        # for i, shift in enumerate(shifts):
        #     for j in range(shift[0], shift[1] + 1):
        #         if shift[2] == 1:
        #             moves[j] += 1
        #         else:
        #             moves[j] -= 1
        
        # ans = ""
        # for i, move in enumerate(moves):
        #     index = (ord(s[i]) - 97 + move) % 26
        #     ans += alphabet[index]

        # return ans

        move = [0] * (len(s) + 1)

        #누적합을 통해 계속해서 + (또는 -) 효과를 가져갈 수 있음
        #효과가 끝나는 index인 end+1에 효과가 상쇄될 수 있도록 보수를 더해두기
        for start, end, d in shifts:
            if d == 1:
                move[start] += 1
                move[end + 1] -=1
            else:
                move[start] -= 1
                move[end + 1] += 1
        
        for i in range(1, len(move)):
            move[i] += move[i - 1]

        ans = []
        for i in range(len(s)):
            new_char = chr((ord(s[i]) - 97 + move[i]) % 26 + 97)
            ans.append(new_char)
        
        return "".join(ans)
