import sqlite3
import hashlib
import argparse
import random
import os

# Connect sql file with python file
conn = None
# Execute the sql file in python
cursor = None


def open_and_create(path):
    """Connect the Pyhton file with the SQL file.
       Try to select all the users from the table,
       otherwise it creates the table.

       Keyword arguments:
       path -- Location of the database file
    """
    global conn
    global cursor

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    try:
        # Select all users from user table
        cursor.execute("SELECT * FROM user")

    except sqlite3.OperationalError:
        # If table does not exist, we create one
        create_user_table()


def create_user_table():
    """Creates the TABLE user in the SQL file
    """
    global conn
    global cursor

    # Create table
    cursor.execute(
        '''CREATE TABLE user(username TEXT, password TEXT,
           salt INT, PRIMARY KEY(username))''')


def save_new_username(username, password):
    """Saves in the SQL databse the:
       - username
       - digest (the hash of password + salt)
       - salt (random number choosen between 1 and 9999)

       Keyword arguments:
       username -- The username choosen by the user
       password -- The password choosen by the user
    """
    global conn
    global cursor

    # Create a random salt
    salt = random.randint(1, 9999)
    password = str(salt) + password

    # Compute hash of the password
    digest = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # Prepared statement to avoid sql injection
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))

    conn.commit()


def check_for_username(username, password):
    """Checks if the credentials given by the username are correct

       Keyword arguments:
       username -- The username choosen by the user
       password -- The password choosen by the user
    """
    global conn
    global cursor

    # Prepare statement to avoid sql injection
    rows = cursor.execute("SELECT * FROM user WHERE username = ?",
                          (username,))
    conn.commit()
    results = rows.fetchall()

    password = str(results[0][2]) + password

    # Compute hash of the password
    digest = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # Check if computed digest is equal to stored digest
    if digest == results[0][1].lower():
        return True
    else:
        return False


def parse_argument():
    """Parses all the arguments passed by the user
    """
    parser = argparse.ArgumentParser()

    # Command to add a user
    parser.add_argument("-a", help="add a username (requires -p)",
                        required=False)

    # Command to check user credentials
    parser.add_argument("-u",
                        help="check for username and password, (requires -p)",
                        required=False)

    # Command for the user password
    parser.add_argument("-p", help="the username password ", required=True)

    # Command to display all users
    parser.add_argument("-d", help="display all users, requires admin user",
                        required=False, action="store_true")

    return parser.parse_args()


def display_all_users():
    """Displays all the username for all the users.

       This function is available only for admin user.
    """
    rows = cursor.execute("SELECT username FROM user")
    conn.commit()
    results = rows.fetchall()

    print("Users: ")
    for row in results:
        print(row[0])


if __name__ == "__main__":

    path = os.path.abspath(os.path.join(
                           os.getcwd(), 'covid_package/database/database.db'))

    open_and_create(path)

    args = parse_argument()

    if args.a and args.p:
        save_new_username(args.a, args.p)
    elif args.u and args.p and not args.d:
        check_for_username(args.u, args.p)
    elif args.u == "admin" and args.p and args.d:
        if check_for_username(args.u, args.p) is True:
            display_all_users()
        else:
            print("Wrong password")
    else:
        print("Something went wrong, type -h for help")
    conn.close()
