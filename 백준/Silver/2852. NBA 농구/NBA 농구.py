n = int(input())
one_score = 0
two_score = 0
one_time = 0
two_time = 0

last_time = 0

for i in range(n):
	num, time = input().split()
	m, s = map(int, time.split(':'))

	t = 60*m + s - last_time
	last_time = 60*m + s

	if one_score>two_score: one_time+=t
	if two_score>one_score: two_time+=t

	if num=='1': one_score+=1
	if num=='2': two_score+=1

if one_score>two_score: one_time+=48*60 - last_time
if two_score>one_score: two_time+=48*60 - last_time

print('{0:02d}:{1:02d}'.format(int(one_time/60), one_time%60))
print('{0:02d}:{1:02d}'.format(int(two_time/60), two_time%60))