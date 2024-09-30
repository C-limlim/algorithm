# n개의 정수 수열
# 연속된 몇개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
# 단 수는 한개이상 선택해야함

n = int(input())
arr = list(map(int, input().strip().split()))
dp = [0] * n

dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))