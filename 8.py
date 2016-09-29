__author__ = 'student'
n=int(input())
A=[]
k=0
for i in range(n):
    A.extend(list(map(int, input().split())))
t = int (input())
for i in range(0, len(A), 2):
    if A[i]<=t and A[i+1]>=t:
        k+=1
print(k)