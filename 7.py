__author__ = 'student'
A = list(map(int, input().split()))
s=0
k=0
for i in range (len(A)-1):
    if A[i]==2 and A[i+1]!=2:
        A[i]=1
for i in range (len(A)):
    if A[i]!=1:
        s+=A[i]
        k+=1
print(int(s/k))