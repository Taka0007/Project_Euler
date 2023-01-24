num = str(2**1000)
length = len(num)
ans = 0

for i in range(length):
  ans += int(num[i])

print(ans)
