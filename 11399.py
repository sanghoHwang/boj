#n = int(input())
#list = list(map(int, input().split()))
#list.sort() #[1, 2, 3, 4, 5] 

#for i in range(1, n):
 #   list[i] = list[i] + list[i-1] #arr[0]은 안건듬

#print(sum(list))
#=====================================================

n = int(input())
list = list(map(int, input().split()))
list.sort()

temp = 0
sum = 0

for i in list:
    temp += i
    sum += temp

print(sum)
