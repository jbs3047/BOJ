import heapq
n=int(input())
lst=[int(input()) for _ in range(n)]
heapq.heapify(lst)
cnt=0
while len(lst)>1:
    x=heapq.heappop(lst)
    y=heapq.heappop(lst)
    cnt+=x+y
    heapq.heappush(lst,x+y)
print(cnt)