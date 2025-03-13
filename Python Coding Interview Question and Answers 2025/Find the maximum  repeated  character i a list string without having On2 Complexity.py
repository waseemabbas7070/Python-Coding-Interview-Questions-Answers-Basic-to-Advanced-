s = "insshshhhdffhhwehrjrjweje"
ch = {}
for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1  

# print(ch)    
max_char = max(ch,key=ch.get) 
print(max_char)     