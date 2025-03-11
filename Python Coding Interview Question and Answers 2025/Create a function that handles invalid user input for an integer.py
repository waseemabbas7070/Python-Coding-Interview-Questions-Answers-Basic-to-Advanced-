def get_interger(prompt = "Enter an Integer "):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

num = get_interger()
print(f"You entered : {num}" )            