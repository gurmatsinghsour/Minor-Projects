data = {
    "Gurmat Singh" : 12345
}

i = 3
f = 3
while True:
    
    try:
        name = input("Enter your username : ")

    except TypeError:
        print("Please Enter a valid value :")
        
    else:
        if name in data.keys():
            
          break
        else:
            i -= 1
            if i != 0:
                print(f"Wrong username, you have {i} turns left to attempt!")
                continue
            else:
                exit()

        
while True:
    try:
        password = int(input("Enter your password : "))
        if password in data.values():
            print("login sucessful")
            break
        else:
            f -= 1
            if f != 0:
                print(f"Wrong password, your have {f} turns left to attempt!")
                continue
            else:
                exit() 

               

    except ValueError:
        print("Please enter a valid value.")

    except TypeError:
        print("Please enter a valid value.")   
