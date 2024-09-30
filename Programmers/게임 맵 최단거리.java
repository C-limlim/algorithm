import java.util.Queue;
import java.util.LinkedList;

class Cell {
    private int x;
    private int y;
    
    public Cell(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
}

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        bfs(0, 0, maps);
        answer = maps[maps.length - 1][maps[0].length -1];
        
        if (answer == 1) {
            return -1;
        } else {
            return answer;
        }
    }
    
    static void bfs(int x, int y, int[][] maps) {
        Queue<Cell> q = new LinkedList<>();
        int n = maps.length; int m = maps[0].length;
        int[] dx = {0, 0, -1, 1}; //상하좌우
        int[] dy = {-1, 1, 0, 0};
        
        q.offer(new Cell(x, y));
        
        while(!q.isEmpty()) {
            Cell currCell = q.poll();
            int cx = currCell.getX();
            int cy = currCell.getY();
            
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1){
                    maps[nx][ny] = maps[cx][cy] + 1;
                    q.offer(new Cell(nx, ny));
                }
            }
        }
    }
}