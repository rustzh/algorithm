import math

Happy = ['H', 'A', 'P', 'Y']
Sad = ['S', 'A', 'D']

m = input()

P_H = 0
import math

P_G = 0

for c in m:
	if c in Happy:
		P_H+=1
	if c in Sad:
		P_G+=1

if P_G==0 and P_H==0:
	H = 50
else: 
	H = P_H / (P_H+P_G) * 100 + 0.005

print(f"{math.floor(H * 100) / 100:.2f}")