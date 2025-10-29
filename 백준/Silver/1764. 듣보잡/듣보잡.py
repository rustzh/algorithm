import sys

N, M = map(int, input().split())

no_listen = set()

no_listen_and_look = set()

for i in range(N):
	no_listen.add(sys.stdin.readline().rstrip())

for i in range(M):
	person = sys.stdin.readline().rstrip()

	if person in no_listen:
		no_listen_and_look.add(person)

result = list(no_listen_and_look)
result.sort()
print(len(result))

for person in result:
	print(person)