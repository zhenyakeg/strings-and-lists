__author__ = 'student'
input = open('input5.txt', 'r')
A = input.readline().split()
k, n = int(A[0]), int(A[1])
A = [1]*(n+1)
for i in range(k-1,n):
    A[i+1]=0
    for j in range (k):
        A[i+1]+=A[i-j]

print(A[n])

