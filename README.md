## Task Manager

Welcome to the Task Manager, a simple command-line application for managing tasks and user accounts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Task Manager is designed to help users efficiently manage tasks, including adding new tasks, viewing all tasks, viewing tasks assigned to a specific user, generating reports, and displaying statistics. Additionally, the application supports user registration and login functionalities.

## Features

- **Task Management:**
  - Add new tasks with relevant details such as assigned user, title, description, due date, and completion status.
  - View all tasks to get an overview of the entire task list.
  - View tasks assigned to the logged-in user.

- **User Management:**
  - Register new users with a unique username and password.
  - Secure login functionality with three attempts allowed.

- **Reports and Statistics:**
  - Generate task overview reports, including total tasks, completed tasks, uncompleted tasks, and overdue tasks.
  - Generate user overview reports for the admin, showing task assignment statistics for each user.
  - Display additional statistics such as the number of users and tasks.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd task-manager
   ```

3. Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

4. Run the application:

   ```bash
   python task_manager.py
   ```

## Usage

- Follow the on-screen prompts to login, register a new user, or exit the program.
- After logging in, you can perform various tasks using the main menu options:
  - **Adding a Task (a):** Add a new task with relevant details.
  - **Viewing All Tasks (va):** Display all tasks in the task list.
  - **Viewing My Tasks (vm):** View tasks assigned to the logged-in user.
  - **Generating Reports (gr):** Generate task and user overview reports.
  - **Displaying Statistics (ds):** Display additional statistics (admin only).
  - **Exiting (e):** Exit the program.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as needed.
```
