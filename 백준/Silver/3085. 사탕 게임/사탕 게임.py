import copy

N = int(input())
candy = [list(input()) for _ in range(N)]
candy_col = []

row_long = [0 for _ in range(N)] 
col_long = [0 for _ in range(N)]

def func(info):
	result = 0
	tmp = 0
	e = info[0]

	for k in range(N):
		if e == info[k]:
			tmp += 1
			if k != N-1:
				continue
		result = max(result, tmp)
		tmp = 1
		e = info[k]	

	return result

for j in range(N):
	info = []
	for i in range(N):
		row_long[i] = func(candy[i])
		info.append(candy[i][j])
	col_long[j] = func(info)
	candy_col.append(info)
result = max(max(col_long), max(row_long))

for i in range(N):
	for j in range(N):	
		if j+1 < N and candy[i][j+1]!=candy[i][j]:
			rowi = copy.deepcopy(candy[i])
			rowi[j+1], rowi[j] = rowi[j], rowi[j+1]
			colj = copy.deepcopy(candy_col[j])
			coljj = copy.deepcopy(candy_col[j+1])
			colj[i], coljj[i] = coljj[i], colj[i]

			result = max(result, func(rowi), func(colj), func(coljj))
		if i+1 < N and candy[i+1][j]!=candy[i][j]:
			rowi = copy.deepcopy(candy[i])
			rowii = copy.deepcopy(candy[i+1])
			rowi[j], rowii[j] = rowii[j], rowi[j]
			colj = copy.deepcopy(candy_col[j])
			colj[i], colj[i+1] = colj[i+1], colj[i]

			result = max(result, func(rowi), func(rowii), func(colj))
print(result)