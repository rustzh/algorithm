from itertools import combinations

n, m = map(int, input().split())
maps = [] # 도시 정보 입력할 리스트

# 도시 정보 입력받기
for i in range(n):
	maps.append(list(map(int,input().split())))

# 집과 치킨집의 위치 각각 저장
house = []
chiken = []

for i in range(n):
	for j in range(n):
		if maps[i][j]==1: house.append([i,j])
		if maps[i][j]==2: chiken.append([i,j])

# 집의 모든 치킨 거리 저장
chiken_distance = []

for i in range(len(house)):
	dis = []
	for j in range(len(chiken)):
		dis.append(abs(house[i][0]-chiken[j][0]) + abs(house[i][1]-chiken[j][1]))
	chiken_distance.append(dis)

# 조합을 이용하여 m개 추출하며 최솟값 
arr = [i for i in range(len(chiken))]
result = 10000

for comb in combinations(arr, m):
	city_cd = 0
	for i in range(len(house)):
		min_cd = 100
		for j in range(len(chiken)):
			if j in comb:
				if chiken_distance[i][j]<min_cd:
					min_cd = chiken_distance[i][j]
		city_cd+=min_cd
	if city_cd<result:
		result=city_cd

print(result)