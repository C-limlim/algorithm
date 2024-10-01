
import java.util.*;

class Solution { 
    static ArrayList<String> answers = new ArrayList<>();
    public String[] solution(String[][] tickets) {
        boolean[] visited = new boolean[tickets.length];
        
        dfs(0, "ICN", "ICN", visited, tickets);
        
        if (answers.size() > 1) {
            Collections.sort(answers);
        }
        
        String[] answer = answers.get(0).split(" ");
        return answer;
    }
    
    static void dfs(int count, String depart, String path, boolean[] visited, String[][] tickets) {
        if (count == tickets.length) {
            answers.add(path);
        }
        
        for (int i = 0; i < tickets.length; i++) {
            // 이 티켓 안썼고 & 시작지가 맞으면
            if(!visited[i] && tickets[i][0].equals(depart)) {
                visited[i] = true;
                String dest = tickets[i][1];
                dfs(count + 1, dest, path + " " + dest, visited, tickets);
                visited[i] = false;
            }
        }
        
    }
}