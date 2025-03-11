def read_file(filename):
    with open(filename,'r') as file:
        content = file.read()
        print(content)

filename = 'example.txt'
read_file(filename)