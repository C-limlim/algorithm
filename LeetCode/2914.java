// greedy & string
// 최소한의 변경으로 even-length substring이 0 또는 1로만 이루어진 문자열 만들기
// 따라서 length 2인 substring의 문자를 같게 맞춰주면 됨

class Solution {
    public int minChanges(String s) {
        int changes = 0;

        for (int i = 0; i < s.length(); i+= 2) {
            char first = s.charAt(i);
            char second = s.charAt(i+1);

            if (first != second) {
            changes++;
        }
        }

        return changes;
    }
}
