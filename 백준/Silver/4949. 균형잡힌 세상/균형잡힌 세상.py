from collections import deque

a = ['(', ')', '[', ']']

while True:
	lst = input()
	st = deque()

	if lst=='.': break

	for i in range (100):
		if lst[i] in a:
			if not st:
				st.append(lst[i])
			elif st[-1]=='(' and lst[i]==')':
				st.pop()
			elif st[-1]=='[' and lst[i]==']':
				st.pop()
			else:
				st.append(lst[i])

		if lst[i]=='.':
			break

	if st: 
		print('no')
	else:
		print('yes')