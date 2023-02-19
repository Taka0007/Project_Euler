import sympy

for i in range(1,10000000):
    
  num = int((i*(i+1))/2)
  if len(sympy.divisors(num))>=501:
    print(num)
    break
