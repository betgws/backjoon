import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input())), i)

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - 1:
        Max = sorted_A[i][1] - 1

print(Max+1)