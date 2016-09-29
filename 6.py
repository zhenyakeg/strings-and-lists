__author__ = 'student'
n = int(input())
A = list(map(int, input().split()))
m=min(A)
k=0
while k<n//2:
    m+=1
    if m in A:
        k+=1
print(m)