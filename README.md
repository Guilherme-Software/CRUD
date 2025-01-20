# User CRUD System

This is a simple CRUD (Create, Read, Update, Delete) system built with Python and SQLAlchemy to manage user registration in a MySQL database. The application allows users to create, read, update, and delete user records in the database.

## Features

- *Create:* Add a new user to the database.
- *Read:* Retrieve user details by username or display all users.
- *Update:* Change the password of an existing user.
- *Delete:* Remove a user from the database.

## Requirements

- Python 3.x
- MySQL
- SQLAlchemy
- PyMySQL

## Installation

### 1. Clone this repository:

### 2. Set up your environment:

Create a virtual environment (optional but recommended)

### 3. Install dependencies:

  - SQLAlchemy
  - PyMySQL

### 4. Set up the database:
Make sure you have MySQL running locally or remotely, and create a database.

In line 5 of the app.py, you need to change:
**engine = create_engine(f"mysql+pymysql://user:password@host/database")**
To match your MySQL credentials and database details:

user: The username for your MySQL database (e.g., root).
password: The password for the MySQL user.
host: The address of the MySQL server (e.g., localhost if running locally).
database: The name of the database you want to connect to (e.g., mydb).
For example

### 5. Run the application:

Run the Python script to start the CRUD application:

### 6. Interact with the application:

The program will prompt you with options to create, read, update, or delete a user.

## Code Explanation

### Database Model: Register

The Register class maps to the register table in the MySQL database and contains the following fields:

- user: The username (primary key).
- email: The user's email address (unique).
- password: The user's password (hashed if desired).

### CRUD Functions

- **register_user()**: Adds a new user to the database.
- **read_user()**: Retrieves a user by username or displays all users.
- **update_user()**: Updates the password of an existing user.
- **delete_user()**: Deletes a user from the database.

## Contributing

Feel free to fork the repository and submit pull requests with bug fixes or enhancements.
