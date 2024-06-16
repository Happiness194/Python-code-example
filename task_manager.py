from datetime import datetime

# This program will allow the user to login,register user,add task,view all tasks, view my task and to exit the program,
# Helpfull links:
''' https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
    https://stackoverflow.com/questions/68962951/verifying-username-and-password-in-a-text-file-in-python
    https://stackoverflow.com/questions/61245970/i-am-trying-to-print-all-of-the-logged-in-users-tasks-from-a-filetasks-txt-th
    https://stackoverflow.com/questions/78013100/creating-a-login-program-using-a-text-file'''

# Open text file to read, replace,strip and split lines
data_store = {}
with open("user.txt") as file:
    lines = (file.readlines())
    lines = [line.replace(' ', '')for line in lines]
for line in lines:
    username, password = line.strip().split(',')
    data_store[username] = password

# Open txt file to read lines
with open("tasks.txt", "r") as file:
    data = (file.readlines())

# This will allow the user to login
# Then read username and password from the user.txt file
# Then use conditional statement to validate username and password
while True:
    print("\nPlease login first by entering your credentials!")
    current_username = input("Please enter your username: ")
    current_password = input("Please enter your password: ")
    if current_username not in data_store.keys():
        print("Username is incorrect, please try again")
        continue
    elif data_store[current_username] != current_password:
        print("Password is incorrect, please try again")
        continue
    else:
        print("You are logged in!")
        break

# If username is equal to admin display first menu option
# If username is already registered, select from the second menu option
while True:
    if current_username == 'admin':
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds -  display statistics      
        e - Exit
        : ''').lower()

    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

# If r is chosen, admin must create a new user credentials
    if menu == 'r':
        new_user = input("Please enter username: ")
        new_password = input("Please enter password: ")
        confirm = input("Please re-enter your password: ")
        if new_password == confirm:
            if new_user in data_store.keys():
                print("This user already exist, you need to try again")
                continue
            print("Credentials have been successfully added")
            try:    
                with open("user.txt", "a")as file:
                    file.write(f"\n{new_user}, {new_password}")
            except FileNotFoundError:
                    print("The file does not exist, credentials cannot be saved, please try again\n")            
                    continue
        
        else:
            print("Re-entered an invalid password, try again")

# If a is chosen, the user already have credentials and now can add tasks
    elif menu == 'a':
        now = datetime.now() # current date
        name = input("Please enter users name to assign task: ")
        title = input("Please enter task title: ")
        task_description = input("Please enter task description: ")
        complete = ("No")
        due_date = input("Please enter date in this format 17 May 2024: ")
        current_date = date_time = now.strftime("%d %B %Y")
        try:
            with open("tasks.txt", "a") as file:
                file.write(f"\n{name}, {title}, {task_description}, {due_date}, {current_date}, {complete} ")
        except FileNotFoundError:
            print("The file is missing")

# If va is chosen, the user can view all tasks in the system
    elif menu == 'va':
        for task in data:
            show_info = " "
            show_split = task.split(", ")            
            print(u'\u2500' *80)
            show_info += f"Assigned To: \t\t{show_split[0]}\n"
            show_info += f"Task: \t\t\t{show_split[1]}\n"
            show_info += f"Task Description: \t{show_split[2]}\n"
            show_info += f"Due Date: \t\t{show_split[3]}\n"
            show_info += f"Current Date: \t\t{show_split[4]}\n"
            show_info += f"Task Completed: \t{show_split[5]}"
            print(show_info)
            print(u'\u2500' *80)        

# If vm is chosen, you can only view the task assigned to you only (specific user)
    elif menu == 'vm':

        for task in data:
            show_info = " "
            show_split = task.split(", ")
            
            if show_split[0] == current_username:
                print(u'\u2500' *80)
                show_info += f"Assigned To: \t\t{show_split[0]}\n"
                show_info += f"Task : \t\t\t{show_split[1]}\n"
                show_info += f"Task Description: \t{show_split[2]}\n"
                show_info += f"Due Date: \t\t{show_split[3]}\n"
                show_info += f"Current Date: \t\t{show_split[4]}\n"
                show_info += f"Task Completed: \t{show_split[5]}"
                print(show_info)
                print(u'\u2500' *80)

# If ds is chosen, admin can check statistics in user.txt and tasks.txt files
    elif menu == 'ds':
        try:
            with open("user.txt", 'r') as ds:      
                for count, line in enumerate(lines):          
                    pass
                print("The total number of users: ", count+1)
        except FileNotFoundError:
            print("File is missing")

        try:   
            with open("tasks.txt", 'r') as ds:
                for count, line in enumerate(lines):
                    pass
                print("The total number of tasks:", count+1)
        except FileNotFoundError:
            print("File is missing")

# If e is chosen, you are exiting the program
    elif menu == 'e':
        print('Done, bye!')
        exit()       
    else:
        print("You have entered an invalid choice, please try again")