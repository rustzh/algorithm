price = int(input())

m = 1000-price

cnt = 0
cnt += m // 500
m %= 500
cnt += m // 100
m %= 100
cnt += m // 50
m %= 50
cnt += m // 10
m %= 10
cnt += m // 5
m %= 5
cnt += m

print(cnt)