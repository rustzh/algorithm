L = int(input())
A = input()

M = 1234567891

result = 0
for i in range(L):
	a = ord(A[i]) - 96
	result += a * pow(31, i)

print(result % M)