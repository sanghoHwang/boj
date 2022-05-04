T = int(input())
for _ in range(T):
	stack = []
	VPS = True
	for char in input():
		if char == '(':
			stack.append(char)
		else: # 닫는 괄호가 들어올 경우
			if len(stack) > 0: #stack이 비어있지 않으면
				stack.pop() #pop
			else:
				VPS = False #stack이 비어있으면[닫는괄호가 더 많이 들어왔을때]
				break #중지

	if len(stack) > 0:
		VPS = False

	if VPS == True:
		print('YES')
	else:
		print('NO')
	#print('YES' if VPS else 'NO')