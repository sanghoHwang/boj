a, b, c = map(int, input().split())

if(a == b and b == c and c == a): #눈3개일치
   A = 10000 + (a * 1000)
   print(A)
elif a == b or b == c: #눈2개일치
    B = 1000 + (b*100)
    print(B)
elif a == c:
   C = 1000 + (a * 100)
   print(C)
else: #모두 다른 눈
    print(max(a, b, c) * 100)
