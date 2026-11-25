n, m = map(int, input().split())
l = []

for i in range(1, n+1):
    l.append(i)

for i in range(m):
    a, b = map(int, input().split())
    l[a-1:b] = l[a-1:b][::-1]

for i in range(n):
    print(l[i], end=' ')
