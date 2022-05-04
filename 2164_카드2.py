from collections import deque

deq = deque()
N = int(input())
for i in range(1, N+1): # 1, 2, 3 , ... , N
	deq.append(i)
#print(dq)

# 1번과 2번 반복
while len(deq) > 1:
	deq.popleft() # 1번 가장 앞에값 버림
	deq.append(deq.popleft()) # 2번 앞에 값빼서 맨뒤로 넣음
	#print(dq)

print(deq.popleft())