n = int(input())
data = list(map(int, input().split()))
data.append(40)
result = 0
reset = False
num = 0

for i in range (len(data)-1):
    if (data[i+1] == data[i]+1):
        if (not reset):
            reset = True
            num = data[i]
    else:
        reset = False
        if (num == 0):
            num = data[i]
        result += num
        num = 0

print(result)