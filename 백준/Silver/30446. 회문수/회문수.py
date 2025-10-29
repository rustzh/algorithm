n = input()
len_n = len(n)

if len_n == 1:
	result = n

elif len_n == 2:
	result = 9 + int(n[0])
	if n[0] > n[1]:
		result -= 1

else:
	result = 18
	for i in range(10, pow(10, len_n//2+1)+1):
		tmp = str(i)
		a = int(tmp + tmp[len(tmp)-2::-1])
		b = int(tmp + tmp[len(tmp)-1::-1])
		if a <= int(n):
			result+=1
		if b <= int(n):
			result+=1

print(result)