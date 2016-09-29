__author__ = 'student'
A = list(map(int, input().split()))
p=0
n=0
for i in range(len(A)):
    p=A.count(A[i])
    if p>n:
        n=p
        v=A[i]
print(v)