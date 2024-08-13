n, c = map(int, input().split())
m = int(input())
boxes = []
for i in range(m):
    start, end, box = map(int, input().split())
    boxes.append([start, end, box])
boxes.sort(key=lambda x:x[1])

ans = 0

max_delivery = [c] * (n + 1)

for start, end, box in boxes:
    delivery = c
    for i in range(start, end):
        delivery = min(delivery, max_delivery[i])
    delivery = min(delivery, box)
    
    for j in range(start, end):
        max_delivery[j] -= delivery
    
    ans += delivery
    
print(ans)