prime_list = []
i = 2

while len(prime_list) <= 10**4 + 2:
  if isprime(i):
    prime_list.append(i)

  i += 1

print(prime_list[10**4])
