ans = 0
Z = 10**10

for i in range(1,1001):
  ans = ( ans + (i**i)%Z ) % Z

print(ans)
