import math

pre = str(math.factorial(100))
ans = 0

for i in range(len(pre)):
  ans += int(pre[i])

print(ans)
