public class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        answer = dfs(0, 0, target, numbers);
        return answer;
    }
    
    static int dfs(int length, int sum, int target, int[] numbers) {
        if (length == numbers.length) {
            if (sum == target) {
                return 1;
            }
            return 0;
        }
        
        return dfs(length + 1, sum + numbers[length], target, numbers) + dfs(length + 1, sum-numbers[length], target, numbers);
    }
}
