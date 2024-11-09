# n개의 숫자가 있는 배열에서 i < i+1 이어야하고, 모든 숫자들의 and 결과가 x여야 함
# 처음에는 x의 1의 개수를 세어서 n보다 작으면 1을 추가하는 방식으로 풀었는데, 이 방법은 틀림
# 왜냐하면 4(100)같은 경우 7(111)이 아니라 6(110 - 100, 101, 110)으로 막연히 더하면 1이 굳이 없어도 되는 숫자가 빠지게 됨
# 이걸 코드로 어떻게 구현할지 찾아보다가 엄청 멋진 코드 발견
# 계속 다음 num을 +1로 찾아주고 or 연산으로 조건에 맞게 해당 num을 조정해줌

class Solution {
    public long minEnd(int n, int x) {
        long num = x;
        for (int i = 0; i < n-1; i++) {
            num = (num + 1) | x;
        }
        return num;
    }
}

class Solution {
    public long minEnd(int n, int x) {
        char[] bits = new char[27];

        for (int i = 26; i >= 0; i--) {
            if ((x & (1 << i)) != 0) {
                bits[26 - i] = '1';
            } else {
                bits[26 -i] = '0';
            }
        }
        System.out.println(Arrays.toString(bits));

        int index = 26;
        n--;
        while (n > 0) {
            if (bits[index] == '0') {
                bits[index] = '1';
                n--;
            }
            index--;
        }
        String binary = String.valueOf(bits);
        return Integer.parseInt(binary, 2);
    }
}