def read_file(filename):
    try:
        with open(filename,'r') as file:
            count = read_file()
        print(count)
    except FileNotFoundError:
         print(f"Error: The file '{filename}' was not found.") 

filename = 'abc.txt'
read_file(filename)        
