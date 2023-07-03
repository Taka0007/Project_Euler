def collatz_length(N):
  length = 1
  
  while N!=1:
    
    if N%2==0:
      N = int(N/2)
      length+=1
      
    else:
      N = 3*N +1
      length+=1

  return length
  
ans = 1
length = 1

for i in range(2,1000000+1):
  if length <= collatz_length(i):
    length = collatz_length(i)
    ans    = i

print(ans)
