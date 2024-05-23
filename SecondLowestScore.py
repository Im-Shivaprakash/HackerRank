#Second lowest score

names=[]
marks=[]
for i in range(int(input())):
    name=input()
    mark=float(input())
    names.append(name)
    marks.append(mark)
    
true=[*set(marks)]
true.sort()
s=true[1]
h=[]
for i in range(len(marks)):
    if s==marks[i]:
        h.append(i)
    i+=1
res=[]    
for k in h:
    res.append(names[k])
res.sort()
for g in range(len(res)):
    print(res[g])
