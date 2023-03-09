def total(n):
    temp = []
    for i in range(n+1):
        temp.append(i)
    return (sum(temp))

def den(n):
    cd = []
    for i in range(1,n+1):
        if n%i==0:
            cd.append(i)
    return cd

print(total(10))
print(den(32))