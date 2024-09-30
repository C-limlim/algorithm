import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        //target이 word에 없으면 return 0
        List<String> wordsList = new ArrayList<>(Arrays.asList(words));
        //List<String> wordsList = Arrays.asList(words); 초기 선언 후 삽입삭제 불가능
        if(!wordsList.contains(target)) {
            return 0;
        }
        
        answer = bfs(begin, target, wordsList);
        return answer;
    }
    
    static int bfs(String begin, String target, List<String> wordsList) {
        Queue<String> q = new LinkedList<>();
        wordsList.add(begin);
        int n = wordsList.size();
        int[] count = new int[n];
        
        q.offer(begin);
        
        while(!q.isEmpty()) {
            String curr = q.poll();
            int currIdx = wordsList.indexOf(curr);
            
            if (curr.equals(target)) {
                return count[currIdx];
            }
            
            for (int i = 0; i < n; i++) {
                if (wordsList.get(i) == curr) {
                    continue;
                }
                
                if (count[i] != 0) {
                    continue;
                }
                
                //만약 한글자 차이나면
                //걔의 count를 +1하고 queue에 넣음
                int difference = 0;
                char[] currChars = curr.toCharArray();
                char[] adjChars = wordsList.get(i).toCharArray();
                for (int j = 0; j < begin.length(); j++) {
                    if (currChars[j] != adjChars[j]) {
                        difference += 1;
                    }
                }
                
                if (difference == 1) {
                    count[i] = count[currIdx] + 1;
                    q.offer(wordsList.get(i));
                }
            }
        }
        return 0;
    }
}