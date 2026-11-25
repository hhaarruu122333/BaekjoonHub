n, m = map(int, input().split())

l = []
for i in range(1, n+1):
    l.append(i)

for i in range(m):
    a, b = map(int, input().split())
    tmp = l[a-1]
    l[a-1] = l[b-1]
    l[b-1] = tmp

for i in range(n):
    print(l[i], end=' ')
