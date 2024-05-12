#나무자르기
#h를 지정하고 한줄에 연속해 있는 나무를 모두 절단. 
#h보다 작으면 잘리지 않음. 그리고 잘린부분 기준 위의 나무를 가져감 
#적어도 m만큼을 가져가기 위한 h의 최댓값

n, m = map(int, input().split())
trees = list(map(int, input().split()))
ans = 0

low = 0
high = max(trees)

while low <= high:
    
    mid = (low + high) // 2
    sum = 0
    for tree in trees:    
        if tree > mid:
            sum += tree - mid
    
    
    #필요한 양이거나 그 이상이라면 h의 크기를 높여야 함
    if sum >= m:
       low = mid + 1
    else:
        #필요량보다 나무가 부족하다면 한칸 낮춰야함
        high = mid - 1

ans = high
                     
print(ans)
