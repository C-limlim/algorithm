import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] numbers) {
        String[] stringArray = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
        
        Arrays.sort(stringArray, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String o1o2 = o1 + o2;
                String o2o1 = o2 + o1;
                return o2o1.compareTo(o1o2);
            }
                
        });
        if (isAllZero(stringArray)) {
            return "0";
        }
        
        String answer = String.join("", stringArray);
        return answer;
    }
    
    private static boolean isAllZero(String[] array) {
        for (String c : array) {
            if (!c.equals("0")) {
                return false;
            }
        }
        return true;
    }
}