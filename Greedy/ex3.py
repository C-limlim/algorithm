#문제: 1이 될 때까지
# n이 1이 되게하는 최소 횟수 구하기
# 1, 2 둘중 하나를 선택
# 1. n -1
# 2. n / k (n이 k의 배수일때만 가능)

#해결방법
#n을 k의 배수로 만들어서 나눠버린다.

n, k = map(int, input().split(" "))
count = 0

count += n % k
n -= count

count += n // k

print(count)