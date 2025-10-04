n = int(input())

s = 0
b = 0
l = 0
p = 0

for i in range(n):
    a, c = input().split()
    if (a == 'STRAWBERRY'):
        s += int(c)
    if (a == 'BANANA'):
        b += int(c)
    if (a == 'LIME'):
        l += int(c)
    if (a == 'PLUM'):
        p += int(c)

if ((s==5) or (b==5) or (l==5) or (p==5)):
    print("YES")
else:
    print("NO")