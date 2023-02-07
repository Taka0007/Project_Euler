num = []

for a in range(2,100+1):
  for b in range(2,100+1):

    temp = a**b
    num.append(temp)

print(len(set(num)))
