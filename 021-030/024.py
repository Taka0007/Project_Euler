import itertools

print(*list(itertools.permutations(range(10)))[1000000-1] , sep='')
