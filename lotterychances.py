from numpy import random
n = 0
t = 0
while n == 0:
    t = t + 1
    print(t)
    x = list(range(1,50))
    y = random.choice(x,6)
    a = list(y)
    z = [3,5,10,12,13,18]
    a.sort()
    z.sort()
    if a == z:
        n = n + 1
        print("Su combinacion ganadora ha sido la número:",t)
