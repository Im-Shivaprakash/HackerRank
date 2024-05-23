#Print Weird or not

n=int(input())
if n%2!=0 :
    print("Weird")
elif n%2==0:
    if n<5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif 20<n<=100:
        print("Not Weird")