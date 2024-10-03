import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0] - 1;
            int end = commands[i][1] - 1;
            int target = commands[i][2] - 1;
            
            int[] sliced = sliceArrayByIndex(start, end, array);
            Arrays.sort(sliced);
            answer[i] = sliced[target];
        }
        
        return answer;
    }
    private static int[] sliceArrayByIndex(int start, int end, int[] array) {
        int newArrayLength = end - start + 1;
        int[] newArray = Arrays.copyOfRange(array, start, end + 1);
        return newArray;
    }
}