students = []

def program_loop():
    perm_count = 0
    while perm_count<10:
        action()

def action():
    print("""
 -----------------------------------------
|  -------------------------------------  |
| | Enter 1 : To Add Student's List     | |
| | Enter 2 : To Show Student's List    | |
| | Enter 3 : To Search a Student       | |
| | Enter 4 : To delete a Students data | |
| | Enter 5 : To update a data          | |
| | Enter 6 : Exit                      | |
|  -------------------------------------  |
 -----------------------------------------
		""")
    choice_code = input("Enter your choice code: ")
    choice_code=int(choice_code)
    if choice_code ==1:
        add()
    elif choice_code ==2:
        show_all()
    elif choice_code ==3:
        search()
    elif choice_code ==4:
        delete()
    elif choice_code ==5:
        update()
    elif choice_code ==6:
        exit()
    else:
        print("Invalid Input")
        



def add():
    count=input("\nHow many students data do you wanna add: ")
    if count.isdigit():
        count=int(count)
        count_add = 0
        while (count_add<count):
            name_add = input('\nEnter the full name of the student: ')
            students.append(name_add)
            age_add = input('Enter the age of the student: ')
            students.append(age_add)
            div_add = input('Enter the division of the student: ')
            students.append(div_add)
            cgpa_add = input('Enter the cgpa of Student: ')
            students.append(cgpa_add)
            count_add+=1
    else:
        print('Invalid Input')
        add()
     
            
        
def show_all():
    count_temp = len(students)
    count = 0
    Srno = 1
    while(count<count_temp):
        print('\n')
        print(f"Student no. {Srno}")
        print(f'Name of the student is: {students[count]}')
        count=count+1
        print(f'Age of the student is: {students[count]}')
        count=count+1
        print(f'Division of the student is: {students[count]}')
        count=count+1
        print(f'CGPA of the student is: {students[count]}')
        count=count+1
        Srno = Srno + 1
                


    
def search():
    print("\nRemark!!!  Search the student by its full name")
    search_name = str(input("Enter the full name: "))
    for count in students:
        if search_name == count:
            flag=1
            break
        else:
            flag=0
            
    if flag==1:
        print("\nThe name exists!!")
        index = students.index(search_name)
        print(f'Name of the student is: {students[index]}')
        index=index+1
        print(f'Age of the student is: {students[index]}')
        index=index+1
        print(f'Division of the student is: {students[index]}')
        index=index+1
        print(f'CGPA of the student is: {students[index]}')
        index = index+1
        print("\n")
    else:
        print("The name does not exist!!")
          
          

def delete():
    del_name = str(input('\nEnter the full name of the students to delete: '))
   
    for count in students:
        if count == del_name:
            flag=1
            break
        else:
            flag=0
    
    if flag == 1:
        print('Student found !!!')
        index = students.index(del_name)
        for x in range(1,5):
            students.pop(index)
        
        print('Student data removed')
    else:
        print('Student not found !!!')


def update():
    
    sr_no = input('Enter the Sr no. of the student you want to update: ')
    if sr_no.isdigit():
        sr_no=int(sr_no)
        if sr_no <= len(students)/4:
            print('''What data of student do you wanna change:
                   1. Name of the student
                   2. Age of the student
                   3. Division of the student
                   4. CGPA of the student''')
            update_choice = input('Enter your choice: ')
            update_choice = int(update_choice)
            if update_choice == 1:
                update_name = input('Enter the new name of the student: ')
                students[(sr_no-1)*4] = update_name
                print('The name has been updated')
            elif update_choice == 2:
                  update_roll = input('Enter the new roll no. of the student: ')
                  students[(sr_no-1)*4+1] = update_roll
                  print('The roll no. has been updated')
            elif update_choice == 3:
                  update_div = input('Enter the new division of the student: ')
                  students[(sr_no-1)*4+2] = update_div
                  print('The division has been updated')
            elif update_choice == 4:
                  update_cgpa = input('Enter the new cgpa of the student: ')
                  students[(sr_no-1)*4+3] = update_cgpa
                  print('The cgpa has been updated')
            else:
                print('Invalid Input!!!')
                
        else:
            print('Invalid Input!!!')
    else:
        print('Invalid Input!!!')
        update()
            
        

Admin = {
    "Gurmat Singh" : "00152",
    "Siddharth Singh" : "00153",
    "Vinit Sharma"  : "00154",
    "Priyam"  : "00155" 
}

user_name = input("Please, Enter your username : ")

while True:
    i=3
    if user_name in Admin.keys():
        user_pass = input(f"Welcome {user_name}! Please enter your password : ")
        if user_pass in Admin.values():
            print ("\n\nYou have sucessfully logged in!")
            print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System=========|
 |=======================OF TCET========================|
 |======================================================|
  ------------------------------------------------------


  """)
            program_loop()
                  
    else:
        if user_pass not in Admin.values():
            i = 3 
            print(f'''
You have entered the wrong password, 
Please retry and
you have {i}! turns left to enter your pass''')
            print("")
            user_pass = input(f"{user_name}! Please enter your password again : ")
            if user_pass in Admin.values():
                print(f"\n\nWelcome {user_name}!")

                print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System=========|
 |=======================OF TCET========================|
 |======================================================|
  ------------------------------------------------------


  """)
                
                program_loop()

                
            else: 
                i -= 1
                print(f'''
You have entered the wrong password, 
Please retry and
you have {i}! turns left to enter your pass''')
                print("")
                user_pass = input(f"{user_name}! Please enter your password again : ")
                if user_pass in Admin.values():
                    print(f"\n\nWelcome {user_name}!")

                    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System=========|
 |=======================OF TCET========================|
 |======================================================|
  ------------------------------------------------------


  """)
                    
                    program_loop()

                else: 
                    i -= 1
                    print(f'''
You have entered the wrong password, 
Please retry and 
you have {i}! turns left to enter your pass''')
                    print("")
                    user_pass = input(f"{user_name}! Please enter your password again : ")
                    if user_pass in Admin.values():
                        print(f"\n\nWelcome {user_name}!")

                        print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System=========|
 |=======================OF TCET========================|
 |======================================================|
  ------------------------------------------------------


  """)

                        program_loop()
                        
                    elif i != 0:
        
                        i -= 1 
                        print(f'''
You have entered the wrong password, 
Please retry and 
you have{i} turns left to enter your password)
                        ''')
                        print("")
                        user_pass = input(f"{user_name}! Please enter your password again : ")
                        if user_pass in Admin.values():
                            print(f"\n\nWelcome {user_name}!")

                            print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System=========|
 |=======================OF TCET========================|
 |======================================================|
  ------------------------------------------------------


  """)

                            program_loop()
                            
                        else:
                            print("Incorrect password")
                            exit   
                    else:
                        exit
