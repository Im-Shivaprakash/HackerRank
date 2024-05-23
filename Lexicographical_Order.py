#Must not print the list with N value

x = int(input())
y = int(input())
z = int(input())
n = int(input())
a=[]   
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                b=[]
                b.append(i)
                b.append(j)
                b.append(k)
                a.append(b)
                
print(a)