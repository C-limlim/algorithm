import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int num = sc.nextInt();
        int[] dp = new int[46];
        dp[1] = 1;
        for (int i = 2; i <= 45; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
		System.out.println(dp[num]);
	}

}