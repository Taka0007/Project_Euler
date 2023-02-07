for i in range(1,500):
  for j in range(i,1000):

    if i**2 + j**2 == (1000-i-j)**2:
      ans = i*j*(1000-i-j)
      print(ans)
      break
