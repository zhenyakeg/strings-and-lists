__author__ = 'student'

A = list(map(int, input().split()))

print('**'.join(map(str, A[::-1])))