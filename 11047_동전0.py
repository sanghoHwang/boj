#그리디 문제 -> 최고 수의 배수여야 가능함

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse() # 큰 값부터 살펴 봐야 되기 때문에 전환함
count = 0 # 사용한 동전 갯수 저장 장소
for coin in coins:
	count += K // coin # K[4200] / coin[1000] -> 몫[4]를 ans에 저장 하여 누적함
	K %= coin # 큰 값에서 나눈 나머지 값을 K에 저장함 -> 4200 // 4 -> 200이 K에 저장됨

print(count)