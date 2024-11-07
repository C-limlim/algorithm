//0 이상이 되게 하는 bitwise combination 최대값을 찾는 문제
//이말인즉슨 같은 bit 위치에 1이 있는 숫자들의 개수가 가장 큰 걸 찾으라는 의미다
//이를 위해 24개의 bit를 모두 확인하며 1이 있는 숫자들의 개수를 세어준다

class Solution {
    public int largestCombination(int[] candidates) {
        int maxCombination = 0;
        for (int bit = 0; bit <24; bit++) {
            int count = 0;
            for (int num : candidates){
                if ((num & (1 << bit)) != 0) {
                    count++;
                }
            }
            maxCombination = Math.max(maxCombination, count);
        }
       
        return maxCombination;
    }
}