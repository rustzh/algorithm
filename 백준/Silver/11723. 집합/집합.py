import sys

full_S = set(range(1, 21))
S = set()

M = int(sys.stdin.readline())

for i in range(M):
	oper = list(sys.stdin.readline().split())

	if oper[0] == "add":
		S.add(int(oper[1]))

	elif oper[0] == "remove":
		S.discard(int(oper[1]))

	elif oper[0] == "check":
		if int(oper[1]) in S:
			print(1)
		else:
			print(0)

	elif oper[0] == "toggle":
		if int(oper[1]) in S:
			S.discard(int(oper[1]))
		else:
			S.add(int(oper[1]))

	elif oper[0] == "all":
		S = full_S.copy()

	elif oper[0] == "empty":
		S.clear()