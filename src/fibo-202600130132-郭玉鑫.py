a = 0
b = 1
while a<500:
    print(a,end=',')
    temp = a
    a = b
    b = temp + b
