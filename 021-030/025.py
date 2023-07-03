fibo = [1,1]

while True:
  temp = fibo[-1] + fibo[-2]
  fibo.append(temp)

  if len(str(fibo[-1]))==1000:
    print(len(fibo))
    break
