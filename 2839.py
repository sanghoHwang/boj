n = int(input()) #설탕무게 
count = 0 #봉지수

while n >= 0: #설탕무게가 0이상이면
    if n % 5 == 0: #5의 배수이면
        count = count + int(n/5) #몫을 저장
        print(count) 
        break
    n = n - 3 #5로 나눌수없다면 3을 빼서
    count = count + 1 #봉지수 증가
    
else: #설탕무게 측정 X
        print("-1")
        
