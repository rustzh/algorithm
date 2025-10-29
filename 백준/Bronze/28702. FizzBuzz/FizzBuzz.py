arr = [input() for _ in range(3)]

for i in range(3):
	if arr[i].isdigit():
		value = int(arr[i]) + 3-i
		break

if value%3==0 and value%5==0:
	print("FizzBuzz")

elif value%3==0:
	print("Fizz")

elif value%5==0:
	print("Buzz")

else:
	print(value)