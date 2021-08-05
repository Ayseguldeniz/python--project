p = []
n = 100
for i in range(2,n+1):
    prime = True
    for j in range(2,i) :
        if i % j == 0:
            prime = False
    if prime:
        p.append(i)
print("Prime list = ", p)