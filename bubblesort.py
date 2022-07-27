x=int(input())
n=[int(i) for i in input().split()]
x=len(n)
count=0
for i in range(x):
    for j in range(x-1):
        if n[j] > n[j+1]:
            
            n[j] ,n[j+1]= n[j+1],n[j]
            count+=1

print("Array is sorted in",count,"swaps.")
print("First Element:",n[0])
print("Last Element:",n[-1])

