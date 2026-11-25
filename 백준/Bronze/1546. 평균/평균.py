N = int(input())

def new(a, b):
    return (100 * a) / b

l = list(map(int, input().split()))

b = max(l)

total = 0

for i in range(N):
    total += new(l[i], b)

print(total / N)