class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer += 1;
                dfs(i, n, visited, computers);
            }
        }
        return answer;
    }
    
    static void dfs(int curr, int n, boolean[] visited, int[][] computers) {
        visited[curr] = true;
        
        for (int adj = 0; adj < n; adj++) {
            if (adj == curr || visited[adj] == true) { 
                continue;
            }
            if (computers[curr][adj] == 1) {
                dfs(adj, n, visited, computers);
            }
        }
    }
}