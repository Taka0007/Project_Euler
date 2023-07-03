fibo = [1,2]
ans = 2
i = 2

while True:
  X = fibo[i-1] + fibo[i-2]
  fibo.append(X)
  
  if fibo[i]>= 4000000:      
    break
    
  if fibo[i]%2==0:
    ans += fibo[i]
    i += 1

print(ans)
