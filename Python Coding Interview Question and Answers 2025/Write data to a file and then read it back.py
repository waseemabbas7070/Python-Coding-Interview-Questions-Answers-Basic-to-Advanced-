def write_read_file(filename,data):
     # Writing to the file
     with open(filename,'w') as file:
          file.write(data)


           # Reading from the file

     with open(filename,'r')  as file:  
          content = file.read()
          print("File Content:\n",content)

filename =  "wasemm.txt "    
data = "Hello, this is a test file!\nWelcome to file handling in Python."

write_read_file(filename,data)
