class Solution {
    public int solution(int[][] triangle) {
        int[][] sum = new int[triangle.length][];
        for (int i = 0; i < triangle.length; i++) {
            sum[i] = new int[i+1];
        }
        
        sum[0][0] = triangle[0][0];
        
        for (int i = 0; i < triangle.length - 1; i++) {
            for (int j = 0; j <= i; j++) {
                //왼쪽 아래
                if (sum[i+1][j] == 0) {
                    sum[i+1][j] = sum[i][j] + triangle[i+1][j];
                } else {
                    if (sum[i+1][j] < (sum[i][j] + triangle[i+1][j])) {
                        sum[i+1][j] = sum[i][j] + triangle[i+1][j];
                    }
                }
                
                //오른쪽 아래
                if (sum[i+1][j+1] == 0) {
                    sum[i+1][j+1] = sum[i][j] + triangle[i+1][j+1];
                } else {
                    if (sum[i+1][j+1] < (sum[i][j] + triangle[i+1][j+1])) {
                        sum[i+1][j+1] = sum[i][j] + triangle[i+1][j+1];
                    }
                }
            }
        }
        
        int answer = sum[sum.length-1][0];
        for (int i = 1; i < sum.length; i++) {
            if (sum[sum.length-1][i] > answer) {
                answer = sum[sum.length-1][i];
            }
        }
        
        return answer;
    }
}