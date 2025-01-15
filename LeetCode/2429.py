class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        bnum1 = format(num1, 'b')
        bnum2 = format(num2, 'b')

        bit_in_num1 = bnum1.count('1')
        bit_in_num2 = bnum2.count('1')

        if bit_in_num1 == bit_in_num2:
            return num1
        elif bit_in_num1 > bit_in_num2:
            index = 0
            bnum1 = bnum1[::-1].replace('1', '0', bit_in_num1 - bit_in_num2)[::-1]
            return int(bnum1, 2)
        else: #bit_in_num1 < bit_in_num2
            if bnum1.count('0') <= bit_in_num2 - bit_in_num1:
                return int('1' * bit_in_num2, 2)
            else:
                bnum1 = bnum1[::-1].replace('0', '1', bit_in_num2 - bit_in_num1)[::-1]
                return int(bnum1, 2)
