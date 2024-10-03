public import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        
        answer = binarySearch(1, (long) times[times.length -1] * n, times, n);
        return answer;
    }
    
    static long binarySearch(long start, long end, int[] times, int n) {

        while (start <= end) {
            long mid = (start + end) / 2;
            long sum = 0;
        
            for (int i = 0; i < times.length; i++) {
                sum += mid / times[i];
            }
            
            if (sum >= n) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return start;
        
    }
} {
    
}
