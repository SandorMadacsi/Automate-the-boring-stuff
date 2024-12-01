


#Validating for only numbers
while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    print('Invalid input, please try again. \n')
    

#Validating for only letters and numbers
while True:
    pwd = input("Select a password (containing letters and numbers only): ")
    if pwd.isalnum():
        break
    print('Invalid input, please try again. \n')