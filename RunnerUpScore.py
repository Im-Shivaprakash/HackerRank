#Print the runner up score

if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    
a=max(arr1)
arr1.sort()
while a==arr1[-1]:
    arr1.remove(a)

print(arr1[-1])
