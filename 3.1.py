__author__ = 'student'
A = list(map(int, input().split()))
for i in range(len(A)//2):
    print(A[i],A[-1-i], end=' ')
if len(A)%2!=0:
    print(A[len(A)//2])