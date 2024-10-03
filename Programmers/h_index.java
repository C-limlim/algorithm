import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = n;
        
        while (h > 0) {
            if (citations[n - h] >= h) {
                return h;
            }
            h--;
        }
        
        return 0;
    }
}