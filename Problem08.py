N = input()
ans = 0

for i in range(1000-13):
  num =  1

  for j in range(i,i+13):
      num *= int(N[j])

  ans = max(ans,num)

print(ans)
