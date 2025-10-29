a = []

for i in range (9):
    a.append(int(input()))

def findMax(a):
    
    max_number = 0
    max_index = -1

    
    for i in range(len(a)):
        if max_number < a[i]:
            max_number = a[i]
            max_index = i+1
                   
    print(max_number)
    print(max_index)

findMax(a)
