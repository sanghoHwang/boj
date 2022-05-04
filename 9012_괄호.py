# VPS = boolean 값 설정
# 입력값 T설정

T = int(input())
for _ in range(T):
    stack = []
    VPS = True
    for char in input():
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                VPS = False
                break

    if len(stack) > 0:
        VPS = False

    if VPS == True:
        print('YES')
    else:
        print('NO')