"""
반복구간 [삽입, 삭제] -> 배열에서 시간복잡도 O(N)
1.맨 앞에 값 삭제 -> 2.맨 앞의 값을 맨 뒤로 삽입
1, 2번을 진행 하고 나면은 배열의 길이는 n-1임
따라서
문제 에서 n이 최대 500,000이므로 n이 1일때 까지 반복 진행
(N-1) * (1번+2번) // 그런데 1번과 2번이 각각 3번진행 되므로
-> (N-1) * O(3N)
-> O(3N(N-1)) = O(3N^2-3N) [시간복잡도에서는 큰항만 남기므로]
-> 시간복잡도는 O(N^2)인데 이 문제는 2초안에 풀어야 되므로 배열을 사용하는 방법 아웃
"""

"""
큐의 삽입, 삭제 시간 복잡도는 O(1)이므로 큐를 이용 하여 풀어야 됨
"""
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

"""
#배열 사용
N = int(input())
arr = []
for i in range(1, N + 1):
	arr.append(i)
#print(arr)
while len(arr) > 1:
	arr.pop(0)
	arr.append(arr.pop(0))
	#print(arr)

print(arr.pop())
"""