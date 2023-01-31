from sympy.ntheory import factorint

factorized = factorint(600851475143)
ans = max(factorized.keys())

print(ans)
