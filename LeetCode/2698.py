class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans_list = [1]

        for i in range(2, n + 1):
            str_sq = str(i * i)

            def find_candidates(candidates, before_str, str_sq):
                if len(str_sq) == 1:
                    return candidates

                for i in range(1, len(str_sq)):
                    first, second = str_sq[:i], str_sq[i:]
                    candidates.append(before_str + [first, second])
                    candidates = find_candidates(candidates, before_str + [first], second)
                
                return candidates
            
            candidates = find_candidates([], [], str_sq)
            
            for cand in candidates:
                if sum(int(x) for x in cand) == i:
                    ans_list.append(i)
                    break

        return sum([x * x for x in ans_list])
