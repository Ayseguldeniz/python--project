x,y=0,1
fibonacci = []
while y <= 55:
    fibonacci.append(y)
    x,y = y,x+y
print(fibonacci)