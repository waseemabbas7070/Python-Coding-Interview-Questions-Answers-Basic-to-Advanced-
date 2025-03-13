list = [21,1,4,6,7,8,9,90,23,14,55,14]
n = len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
           list[i], list[j] = list[j], list[i]
print(list)

