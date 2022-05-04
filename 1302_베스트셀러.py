#map
#key->책이름(string)
#value->팔린권수(int)
d = dict() # dictionary 생성
for i in range(int(input())):
	book = input() # 책 이름 저장
	if book in d: # 이미 dictionary에 있는 책이라면
		d[book] += 1 #기존에 있던 책 value값 +1
	else: # 새로들어온 책이라면
		d[book] = 1 #새로 들어온 책 value값 +1

#print(d.keys()) # 키값만 모아서 반환해줌
big = max(d.values())  # dictionary에 있는 최대 value값 저장
#print(d.values()) value값만 모아서 반환해줌
#print(d.items()) # 키 + value값을 묶어서 반환해줌
candidate = [] # value가 최대값인 책 저장공간
for key, val in d.items():
	if val == big: # value값이 최대값이랑 같다면
		candidate.append(key) # candidate 배열에 key값 저장
candidate.sort() # 알파벳 순으로 출력하기 위해 오름차순으로 정렬
print(candidate[0]) # 가장 먼저오는 알파벳 값인 key값 출력