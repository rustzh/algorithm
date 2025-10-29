while(True):
	string = input()

	if string == '0':
		break

	else:
		cnt = 0
		for i in range(len(string)//2):
			if string[i] == string[len(string)-(i+1)]:
				cnt+=1
		if cnt == len(string)//2:
			print('yes')
		else:
			print('no')