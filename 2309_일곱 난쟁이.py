from itertools import combinations

heights = [int(input()) for _ in range(9)] #9개의 수를 입력받음
for i in combinations(heights, 7): # 조합된 7개의 값 추출
	if sum(i) == 100: # 조합된 값 중 합이 100인게 있다면
		for j in sorted(i): # 오름 차순으로 정렬
			print(j)
		break # 7개의 추출한 합이 100인 경우가 여러 개일 수 있다면 필요없는 반복구간을 추가로 돌수있기 때문에 1개만 출력하도록 멈춰야된다

"""
# 순열을 사용하지 않은 경우
heights = [int(input()) for _ in range(9)]
heights.sort()
total = sum(heights)

def f():
	for i in range(8):
		for j in range(i+1, 9):
			if total - heights[i] - heights[j] == 100:
				for k in range(9):
					if i != k and j != k:
						print(heights[k])
				return

f()
"""