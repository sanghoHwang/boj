hour, minute = map(int, input().split())
s = int(input())
hour = (hour + int((minute+s)/60)) % 24
minute = int((minute+s)%60)
print(hour,minute)

