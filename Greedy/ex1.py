# 문제: 큰수의 법칙
# n개의 정수 배열이 있을 때, 원소들을 p번 더하여 가장 큰 수 만들기
# 특정 index의 원소는 최대 k번 더할 수 있음
# 2,3,4,5,6 + p=8, k=3 => 66656665 = 46
# 해결방법
# 가장 큰수 K번  + 두번째로 큰수 1번 반복

n, p, k = map(int, input().split(" "))
num = list(map(int, input().split(" ")))

#첫번째, 두번째 큰 원소 구하기
num.sort(reverse=True)
v1, v2 = num[:2]

#값 계산하기
ans = 0
while (p):
    if p - k >= 0:
        ans += k * v1
        p -= k
        if p != 0:
            ans += v2
            p -= 1
    else:
       ans += p * v1
       
#값 계산하는 파트 바꿔쓰기
#결국 (k+1) 개의 합을 하나의 세트로 생각할 수 있으므로, 이 세트가 p에 몇개 들어가는지 생각하기
#세트가 들어가기에 부족한 개수가 남았다면 그건 그냥 큰수로 더해주면 됨
#따라서 큰 수 :count = ((p // (k+1)) * k + p % (k+1))만큼 더해지게 되고
# 작은수는 : count = (p//(k+1)) (== p - count) 만큼 더해지게 됨

# ans += v1 * count
# ans += v2 * (p - count)

print(ans)