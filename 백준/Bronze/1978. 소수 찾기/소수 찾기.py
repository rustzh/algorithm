N = int(input())
numbers = list(map(int, input().split()))
result = 0

for num in numbers:
	cnt = 0
	if num > 1:
		for i in range(2, num):
			if num%i == 0:
				cnt+=1
		if cnt == 0:
			result+=1

print(result)