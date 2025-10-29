import math
import sys

def round_func(num):
	return math.floor(num+0.5)

n = int(sys.stdin.readline().rstrip())

if n == 0:
	print(0)

else:
	users = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
	users.sort()

	except_users = round_func(n*0.15)

	first_user = except_users
	last_user = n-except_users

	print(round_func(sum(users[first_user:last_user]) / (last_user-first_user)))
