import sqlite3
import hashlib 
import argparse
import random
import os

# connect sql file with python file
conn = None  

# execute the sql file in python
cursor = None

def open_and_create(path):
	global conn 
	global cursor

	conn = sqlite3.connect(path)
	cursor = conn.cursor()

	try: 
		# select all users from user table
		cursor.execute("SELECT * FROM user")

	except sqlite3.OperationalError: 
		# if table does not exist, we create one
		create_user_table(conn, cursor)

def create_user_table():
	global conn 
	global cursor

	# create table
	cursor.execute('''CREATE TABLE user
		(username TEXT, password TEXT, salt INT, PRIMARY KEY(username))''')

# insert data inside the table
def save_new_username(username, password):
	global conn 
	global cursor
	
	# create a random salt 	
	salt = random.randint(1, 9999)
	password = str(salt) + password

	# compute hash of the password
	digest = hashlib.sha256(password.encode("utf-8")).hexdigest()

	# prepared statement to avoid sql injection
	cursor.execute("INSERT OR REPLACE INTO user (?,?,?)", 
		(username, digest, salt))

	conn.commit()

def check_for_username(username, password):
	global conn 
	global cursor

	# prepare statement to avoid sql injection
	rows = cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
	conn.commit()
	results = rows.fetchall()

	# get salt of the database and add the given password
	password = str(results[0][2]) + password
	# compute hash of the password
	digest = hashlib.sha256(password.encode("utf-8")).hexdigest()

	# check if computed digest is equal to stored digest
	if digest == results[0][1].lower():
		return True 

	else: 
		return False

def parse_args():
	parser = argparse.ArgumentParser()

	# command to add a user
	parser.add_argument("-a", help = "add a username (requires -p)",
		required = False)

	# command for the user password
	parser.add_argument("-p", help = "the username password ",
		required = True)

	# command to check user credentials
	parser.add_argument("-c", help = "check for a username and a password, (requires -p",
		required = False)

	return parser.parse_args()


args = parse_args()

path = os.path.abspath(os.path.join(os.getcwd(), 'covid_package/data/database.db'))

open_and_create(path)	

if args.a and args.p: 
	save_new_username(args.a, args.p)
elif args.c and args.p: 
	check_for_username(args.c, args.p)
conn.close()

















