# =====importing libraries===========
import os
from datetime import datetime, date

# Date format for task due date and assigned date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Check if tasks.txt file exists, if not, create an empty one
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w", encoding="utf-8") as default_file:
        pass

# Read task data from tasks.txt and populate the task_list
with open("tasks.txt", 'r', encoding="utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []   # Initialized an empty task list.
for t_str in task_data:
    curr_t = {}  # Initialized an empty curr_t dictionary.

    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
# The empty task list is filled with curr_t string values.

# Check if user.txt file exists, if not, create an empty one
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding="utf-8") as default_file:
        default_file.write("admin;password")

# Read user data from user.txt and populate the username_password dictionary
with open("user.txt", 'r', encoding="utf-8") as user_file:
    user_data = user_file.read().split("\n")

username_password = {}
for user in user_data:
    if ';' in user:
        username, password = user.split(';', 1)
        username_password[username] = password.strip()

def check_existing_username(new_username, file_path="user.txt"):
    """
    Check if a username already exists in the user.txt file.

    Parameters:
    - new_username (str): The username to check.
    - file_path (str): The path to the user.txt file. Default is "user.txt".

    Returns:
    - bool: True if the username exists, False otherwise.
    """
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if ',' not in line:
                continue  # Skip lines that do not contain a comma

            stored_username = line.strip().split(',')[0]
            if new_username == stored_username:
                return True
    return False

def login():
    """
    Allow a user to log in. Three attempts are allowed.

    Returns:
    - bool: True if login is successful, False otherwise.
    """
    attempts = 3  # Allow three login attempts
    while attempts > 0:
        existing_user = input("Enter your username: ")
        user_pass = input("Enter your password: ")

        with open("user.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ';' not in line:
                    continue  # Skip lines that do not contain a semicolon

                stored_username, stored_password = line.strip().split(';', 1)
                stored_password = stored_password.strip()

                if existing_user == stored_username and user_pass == stored_password:
                    print("Login successful!")
                    return True
                elif existing_user == stored_username:
                    print("Incorrect password. Please try again.")
                    break  # Break the loop for the current user if username matches
            else:
                print("Invalid username. Please try again.")
                attempts -= 1
                if attempts == 0:
                    print("Too many incorrect attempts. Exiting program.")
                    exit()  # Exit the program after three incorrect attempts

        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            print("Exiting program.")
            exit()  # Exit the program if the user doesn't want to retry

    return False

def reg_user():
    """
    Register a new user. Three attempts are allowed.

    Returns:
    - None
    """
    attempts = 3  # Allow three registration attempts
    while attempts > 0:
        new_username = input("Enter a new username: ")

        if check_existing_username(new_username):
            print("Username already exists. Please choose another one.")
            attempts -= 1
            if attempts == 0:
                print("Too many attempts. Exiting program.")
                exit()  # Exit the program after three unsuccessful attempts
            continue

        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm your password: ")

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            attempts -= 1
            if attempts == 0:
                print("Too many attempts. Exiting program.")
                exit()  # Exit the program after three unsuccessful attempts
            continue

        with open("user.txt", "a", encoding="utf-8") as file:
            file.write(f"{new_username};{new_password}\n")

        print("User registered successfully!")
        break

    retry = input("Do you want to try again? (yes/no): ").lower()
    if retry != 'yes':
        print("Exiting program.")
        exit()  # Exit the program if the user doesn't want to retry

def add_task():
    """
    Add a new task to the task_list.

    Returns:
    - None
    """
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w", encoding='utf-8') as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    """
    Display all tasks in the task_list.

    Returns:
    - None
    """
    print("You selected Viewing all tasks.")
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine(existing_user):
    """
    Display tasks assigned to the logged-in user.

    Parameters:
    - existing_user (str): The username of the logged-in user.

    Returns:
    - None
    """
    print("You selected Viewing my tasks.")
    task_number = 1  # Initialized task number counter

    for t in task_list:
        if t['username'] == existing_user:
            disp_str = f"Task #{task_number}:\n"
            disp_str += f"Title: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Complete: \t {t['complete']}\n"
            print(disp_str)
            task_number += 1
        while True:
            try:
                task_selection = int(input("Enter the task number you want to view (or enter -1 to return to the main menu): "))
                if task_selection == -1:
                    break  # Exit the loop to return to the main menu
                elif 1 <= task_selection <= task_number - 1:
                # Display the selected task
                    selected_task = task_list[task_selection - 1]
                    print(f"You selected Task #{task_selection}:\n")
                    print(f"Title: \t\t {selected_task['title']}\n")
                    print(f"Assigned to: \t {selected_task['username']}\n")
                    print(f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
                    print(f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
                    print(f"Task Description: \n {selected_task['description']}\n")
                    print(f"Complete: \t {selected_task['complete']}\n")

                # Allow the user to mark as complete or edit the task
                edit_option = input("Do you want to mark task as complete (enter 'C') or edit the task (enter 'E')? ").upper()

                if edit_option == 'C':
                    # Mark the task as complete
                    selected_task['complete'] = 'Yes'
                    print("Task marked as complete.")
                elif edit_option == 'E' and selected_task['complete'] != 'Yes':
                    # Edit the task
                    edit_choice = input("To edit assigned username (enter 'U') or due date (enter 'D')? ").upper()
                    if edit_choice == 'U':
                        new_username = input("Enter the new username: ")
                        selected_task['username'] = new_username
                        print("Username updated.")
                    elif edit_choice == 'D':
                        new_due_date = input("Enter the new due date (YYYY-MM-DD HH:MM): ")
                        try:
                            selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            print("Due date updated.")
                        except ValueError:
                            print("Please enter the date in the format YYYY-MM-DD HH:MM.")
                        else:
                            print("Please enter 'U' to edit the username or 'D' to edit the due date.")
                elif edit_option == 'E' and selected_task['complete'] == 'Yes':
                    print("Task has already been completed and cannot be edited.")
                elif edit_option is None:
                    print("Please enter 'C' to mark as complete or 'E' to edit the task.")
                    break  # Exit the loop after marking as complete or editing
                else:
                    print("Invalid task number. Please enter a valid task number.")
            except ValueError:
                print("Please enter a valid task number or -1 to return to the main menu.")

def generate_task_overview_report():
    """
    Generate and write the Task Overview Report to a file.

    Returns:
    - None
    """
    total_tasks = len(task_list)
    completed_tasks = sum(task['completed'] == 'Yes' for task in task_list)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(task['completed'] != 'Yes' and task['due_date'] < datetime.now() for task in task_list)

    with open('task_overview.txt', 'w', encoding='utf-8') as task_file:
        task_file.write("Task Overview Report\n")
        task_file.write("-----------------------------------\n")
        task_file.write(f"Total Tasks: {total_tasks}\n")
        task_file.write(f"Completed Tasks: {completed_tasks}\n")
        task_file.write(f"Uncompleted Tasks: {uncompleted_tasks}\n")
        task_file.write(f"Overdue Tasks: {overdue_tasks}\n")

        # Calculating percentages
        percentage_incomplete = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        task_file.write(f"Percentage of Incomplete Tasks: {percentage_incomplete:.2f}%\n")
        task_file.write(f"Percentage of Overdue Tasks: {percentage_overdue:.2f}%\n")


def generate_user_overview_report(existing_user):
    """
    Generate and write the User Overview Report to a file.

    Returns:
    - None
    """
    total_users = 0

    if existing_user == 'admin':
        total_users = len(username_password.keys())

    with open('user_overview.txt', 'w', encoding='utf-8') as user_file:
        user_file.write("User Overview Report\n")
        user_file.write("-----------------------------------\n")
        user_file.write(f"Total Users: {total_users}\n")
        user_file.write(f"Total Tasks: {len(task_list)}\n")

        for user in username_password.keys():
            user_tasks = [task for task in task_list if task['username'] == user]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(task['completed'] == 'Yes' for task in user_tasks)
            uncompleted_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(task['completed'] != 'Yes' and task['due_date'] < datetime.now() for task in user_tasks)

            user_file.write(f"\nUser: {user}\n")
            user_file.write(f"Total Tasks Assigned: {total_user_tasks}\n")

            if total_user_tasks > 0:
                user_file.write(
                    f"Percentage of Total Tasks Assigned: {(total_user_tasks / len(task_list)) * 100:.2f}%\n"
                )
                user_file.write(
                    f"Percentage of Completed Tasks: {(completed_user_tasks / total_user_tasks) * 100:.2f}%\n"
                )
                user_file.write(
                    f"Percentage of Tasks to be Completed: {(uncompleted_user_tasks / total_user_tasks) * 100:.2f}%\n"
                )
                user_file.write(
                    f"Percentage of Overdue Tasks: {(overdue_user_tasks / total_user_tasks) * 100:.2f}%\n"
                )
            else:
                user_file.write("No tasks assigned to this user.\n")

    print("User Overview Report generated successfully.")


def display_statistics():
    """
    Display additional statistics.

    Returns:
    - None
    """
    task_overview_file_path = 'task_overview.txt'
    user_overview_file_path = 'user_overview.txt'

    if os.path.exists(task_overview_file_path):
        with open(task_overview_file_path, 'r', encoding="utf-8") as task_file:
            print(task_file.read())

    if os.path.exists(user_overview_file_path):
        with open(user_overview_file_path, 'r', encoding="utf-8") as user_file:
            print(user_file.read())

    # Additional statistics
    num_users = len(username_password.keys())
    num_tasks = len(task_list)
    print("-----------------------------------")
    print("Additional Statistics\n")
    print(f"Number of users: {num_users}")
    print(f"Number of tasks: {num_tasks}")
    print("-----------------------------------")

def main_menu(existing_user =None):
    """
    Display the main menu options and perform the selected action.

    Parameters:
    - existing_user (str): The username of the logged-in user.

    Returns:
    - None
    """
    print()
    if not task_list:
        add_task_option = input("No tasks available. Would you like to add one? (yes/no): ").lower()
        if add_task_option == 'yes':
            add_task()
        else:
            return  # Return to the main menu
    menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    if menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(existing_user)

    elif menu == 'gr':
        print("You selected Generating Reports.")
        generate_task_overview_report()
        generate_user_overview_report(existing_user)
    elif menu == 'ds' and existing_user == 'admin':
        print("You selected Displaying Statistics.")
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
        exit()

def main():
    """
    Main function to initiate the task manager program.

    Returns:
    - None
    """
    print("Welcome to The Task Manager!")

while True:
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

    option = input("Enter your option: ")

    if option == '1':
        if login():
            main_menu()
    elif option == '2':
        reg_user()
    elif option == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
