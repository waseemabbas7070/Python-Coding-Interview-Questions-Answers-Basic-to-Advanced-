def count(filename):
    with open(filename,'r') as file:
        return sum(1 for line in file)
    

filename =  "wasemm.txt"
line_count = count(filename)
print(f"Number of lines: {line_count}")