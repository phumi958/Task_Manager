# Reference: Farinaaz Slamang.
# Reference: https://www.geeksforgeeks.org/personalized-task-manager-in-python/?ref=gcse_outind
# Reference: https://www.youtube.com/watch?v=dR_cDapPWyY
# Reference: https://www.youtube.com/watch?v=MYYWnRDP8Q0
# Reference: https://brainly.com/question/33431819?source=regflowPage&cb=1730238299418
# Reference: https://www.studocu.com/en-gb/messages/question/2886782/httpswwwdropboxcomsway0qni2crm3z6btask-manager201pydl0
# Reference: https://www.reddit.com/r/learnpython/comments/x1rt5n/i_have_pylint_errors_please_help/?rdt=54403
# Reference: https://www.youtube.com/watch?v=-AlFiS74aQg
# Reference: Chris Smit
# Create a task manager programme that allows a registered users to login and view tasks.
# Open user.txt in read mode that has all the users that have an account.
# Create a dictionary that will store the username:password as an item.
# User input to checked against dictionary to see if information is in textfile.
# Create functions to register,add tasks,view tasks,view my tasks,display statistics.
# Create a menu function that will filter through users.
# Check for admin user: give authorisation to register new users and view the statistics.

# Place all imports and functions below:
from getpass import getpass
from datetime import date
today = date.today()

# Create a function for registering a new user.
# Request for user input and verify if username is in the user.txt.
# If username is not in user txt, append the user.txt to add the name and password
def register():
    '''Use a while loop to ask for user input until valid user account has been registered '''
# Open user.txt in append + mode to allow for the reading and appending of the text file.
    with open("user.txt", "a+") as user_file:
        f = user_file.readlines()
        for lines in f:
            line = lines.strip()
            line = lines.split(",")

# Use a while loop to ensure that usernames entered are unique.       
        username = input("Please enter user username: ")
        if username.isalpha() and len(username) > 1:
            while username in user.keys():
                print("username exists, try again")
                username = input("Please enter user username: ")
                continue

        password = getpass("Create a password: ")
        password1 = getpass("Confrim password: ")
        
        while password != password1:
            print ("Password does not match, please start over")
            password = getpass("Create a password: ")
            password1 = getpass("Confrim password: ")

# Add the username and password pair to the user.txt.    
        user_file.write("\n")
        user_file.write(username + ", " + password)
        print("Successfully registered")                    
        

# Create a function that will allow the addition of tasks to the task.txt file.
def add_new_task():
    ''' Open tasks text file in append mode, this will allow for the addition of tasks to the text file.'''
    with open("tasks.txt", "a") as task_file:

# Request for user input for all the relevant information.
        responsible_person = input("Enter person who is responsible for the task: ")
        title = input( "Enter task: ")
        task_descr = input("Enter task description: ")
        due_date = input("Enter the date the task is due in this format (10 Oct 2023): ")
        assigned_date = today.strftime("%d %b %Y")
        task_status = "No"

# Add the user input to the tasks textfile.
# Each task should be on a newline thus after therefore we start with a \n.
        task_file.write("\n" + responsible_person + ", ")
        task_file.write(title +"," + " ")
        task_file.write(task_descr + ","+ " ")
        task_file.write(assigned_date+ ","+ " ")
        task_file.write(due_date + "," +" ")
        task_file.write(task_status)
        

# Create a function that allows for the viewing of all tasks that are in the tasks.txt file.
def view_all_tasks():
    '''Open file in read mode and read each line so that we are able to manipulate the strings.''' 

    with open("tasks.txt", "r") as task_file:
        file = task_file.readlines()

# Use a for loop to iterate through each line in the tasks.txt file.
# Use the strip and split method to remove whitespace and split at the comma.
        for line in file:
            file = line.strip()
            file = line.split(",")
            responsible_person,title,date_assigned,due_date,task_descr,task_status = file

# Display tasks to the user in a way whereby they are easy to read.
# Use indexing to ensure that information desplayed is in the correct order.
            print("Task: " + file[1])
            print("Assigned to: " + file[0])
            print("Date assigned: " + file[3])
            print("Due date: " + file[4])
            print("Task complete? " + file[5])
            print("Task description: " + file[2])


# Create a function that views only the tasks of the individual who has looged in
def user_tasks(usrname):
    '''Open the tasks.txt file in reading mode and use the readlines method.'''
    with open( "tasks.txt", encoding ="utf-8") as task_file:
        file = task_file.readlines()
# Use a try and except method to be able to catch any errors that might crash the program.
        try:
            for line in file:
                file = line.strip()
                file = line.split(",")
                responsible_person,title,due_date,date_assigned,task_descr,task_status = file
# Create a condition that only tasks of the responsible person are displayed
                if responsible_person == username:
                    print("Task: " + file[1])
                    print("Assigned to: " + file[0])
                    print("Date assigned: " + file[3])
                    print("Due date: " + file[4])
                    print("Task complete? " + file[5])
                    print("Task description: " + file[2])
        except ValueError:
            print("Error, please check your textfile to ensure 6 variables are in the same line")


# Create a function that will count number of tasks and users from the text files.
def display_stats():
    '''Function that displays user and task stats'''
# Open the tasks.txt file in reading mode.
    with open("tasks.txt","r") as f:
        lines = f.readlines()

# Include a for loop that will iterate through each line
        for line in lines:
            tasks = line.split(",")
            num_of_tasks = len(lines)
        total = num_of_tasks

# Open the user,txt in read mode and count the number of users registered
    with open("user.txt","r") as doc:
        lines = doc.readlines()
        for line in lines:
            num_of_users = len(lines)  # Use the length() method to count each line in the user.txt file.
    
    print("The total amount of users is: ", num_of_users, ", total amount of tasks is:", total)


# ============== Login section =============================
# This section is for loging into the programme.
# Registered users will be able to login into their accounts by entering correct credantials.

# Create an empty dictionary that will be used to store all the usernames and passwords.
user = {}

with open("user.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        keys,values = line.split(",")
        values =values.strip()
        user[keys] = values

# Request for user input for name and password.
# This should be a loop that broken when user inputs a username and password that is in the user.txt file.
while True:
    username = input("Please enter username: ")
    password = input("Please enter password: ")

# Create a conditional statement that verfies that the username and password pair.
    if username in user.keys() and password == user[username]:
        print("login successful")
    elif username and password != user.items():
        print("Username or Password is incorrect. Try again!")
        continue
    break

# ================ Menu section ================================
# Create a menu that will display to the users.
# If user is am admin, their menu will have a extra funtion that counts the total number of users and tasks.
# The admin will also have authority to register new users.
# For others users, the menu will restrict them from registering new users.

# Create a while that will display the menu with different options to the user. 
while True:

# If the user is not an admin this menu will display.
    if username != "admin" and password != "adm1n":
        menu = input("""
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        """)

# If user is the admin this menu will display.
# Menu includes display stats, which will calculate the number of users and tasks.
    else:
        menu = input("""
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        ds - display statistics
        e - exit
        """)

# Create a flow process within the menu
# Using if,elif and else method, call in functions for each options in the menu

    if menu == 'r':
        if username == "admin":
            register()
        else:
            print("You are not authorised")

    elif menu == 'a':
        add_new_task()

    elif menu == 'va':
        view_all_tasks()

    elif menu == 'vm':
        user_tasks(username)

    elif menu == 'ds':
        display_stats()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("Invalid entry")
