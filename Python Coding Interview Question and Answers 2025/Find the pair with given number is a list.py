list = [1,3,5,7,8,9,4]
n = len(list)
s = 10

for i in range(n):
    for j in range(i+1,n):
       if (list[i]+list[j]) == s:
           print(list[i],list[j])
