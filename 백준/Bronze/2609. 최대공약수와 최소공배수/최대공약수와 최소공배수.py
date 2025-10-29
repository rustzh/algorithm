n, m = map(int, input().split())
x = n*m

while(n%m != 0):
	r = n%m
	n = m
	m = r

print(m) 
print(x//m) # 최소공배수 = n*m // 최대공약수