from random import seed, uniform

# work with this variable
n = int(input())
seed(n)
print(uniform(0, 1))
