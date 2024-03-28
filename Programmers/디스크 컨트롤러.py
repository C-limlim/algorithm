#문제: 디스크 컨트롤러 -Heap
#작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리할 때,
#해당 평균값의 정수를 return
#하드웨어가 작업을 수행하고 있지 않을때에는 먼저 요청이 들어온 작업부터 처리

#해결방법: 아 헷갈리네... 먼저끝나는걸 먼저하는건 맞는데. 근데 그때 놀고있으면 들어온걸 처리해야하잖아
#sorted 의 리턴값이 list라는거랑 curr_time을 비교하는 28번째 코드가 없어서 계속 틀렸다.

#다른사람풀이: heapq를 써서 우선순위 큐 구현. 나랑 로직은 똑같은데 간결성이 다르다. ㅠㅠ
# 1. 먼저 job을 나랑 반대로 정렬해두고 - 빨리실행되는순
# 2. 현재시간을 현재시간+걸리는시간 과 도착한 시간 + 걸리는시간 중 max로 설정한다
# 3. 그리고 total time을 계산한다
# 4. 만약에 job이 남아있고 남아있는 job중 가장 빨리 도착한게 현재시간보다 빠르다면(이미 요청되었다면)
#    while로 해당하는 모든 job을 heapq에 넣어준다.
# 5. 만약 task가 남아잇는데 queue 0개라면 맨 앞엣놈 하나 넣어준다.

from collections import deque

def solution(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    # print(jobs)
    total_jobs = len(jobs)
    total_time = 0
    curr_time = 0
    queue = deque([jobs.pop(0)])
    
    while len(jobs) > 0 or len(queue) > 0:    
        #요청이 하나만 있으면 그냥 걔를 수행하면 된다.
        #요청이 여러개 있을 경우 그중 가장 빨리끝나는 놈을 수행한다.
        queue = deque(sorted(queue, key=lambda x: x[1]))
        
        # print('queue: ', queue)
        # print('curr_time: ', curr_time, '| total_time: ', total_time)
            
        job = queue.popleft()
        curr_time = job[0] if job[0] > curr_time else curr_time
        curr_time += job[1]
        total_time += curr_time - job[0] #일 처리한 후 현재 시간 - 요청된 시간
        
        ## job을 처리하는동안 새로 들어온 요청들을 queue에 넣어준다.
        requested_latest_job_id = -1 
        for i, job in enumerate(jobs):
            if job[0] <= curr_time: 
                queue.append(job)
                requested_latest_job_id = i
            else:
                break
        jobs = jobs[requested_latest_job_id + 1:]
        
        #만약 queue가 비어있다면, 가장 빨리 들어오는 요청을 넣어준다.
        #만약 그 시간에 여러개의 요청이 들어왔다면 가장 빨리 끝나는 요청을 수행할것이므로
        #그 요청만 넣어준다. 나머지 요청은 넣어줄 필요 없다.
        if not len(jobs) == 0 and len(queue) == 0:
            queue.append(jobs.pop(0))
                
    # print(total_time)
    return total_time // total_jobs

print(solution([[1, 4], [7, 9], [1000, 3]]))