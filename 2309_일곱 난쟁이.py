from itertools import combinations

heights = [int(input()) for _ in range(9)] #9개의 수를 입력받음
for i in combinations(heights, 7): # 7개의 순열 값 추출
	if sum(i) == 100: # 순열된 값중 합이 100인게 있다면
		for j in sorted(i): # 오름차순으로 정렬
			print(j)
		break # 7개의 추출한 합이 100인 경우가 여러 개일 수 있다면 필요없는 반복구간을 추가로 돌수있기 때문에 1개만 출력하도록 멈춰야된다