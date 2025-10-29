from collections import deque

n = int(input())
stack = []
number = 1
commands = []

for i in range(n):
	num = int(input())

	while number <= num:
		stack.append(number)
		commands.append("+")
		number+=1

	if stack[-1] == num:
		stack.pop()
		commands.append("-")

	else:
		commands.append("NO")
		break

if commands[-1] == "NO":
	print("NO")
else:
	for command in commands:
		print(command)