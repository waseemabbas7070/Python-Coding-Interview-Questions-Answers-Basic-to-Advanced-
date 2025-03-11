def safe_devide(a,b):
    try:
        result = a / b
        print(f" Result : {result}")

    except ZeroDivisionError:
       print("Error: Division by zero is not allowed!")
   
   

safe_devide(10,2)
safe_devide(5,0)        
       

