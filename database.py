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
		create_user_table()

def create_user_table():
	global conn 
	global cursor

	# create table
	cursor.execute('''CREATE TABLE user(username TEXT, password TEXT, salt INT, PRIMARY KEY(username))''')

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
	cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)", (username, digest, salt))

	conn.commit()

def check_for_username(username, password):
	global conn 
	global cursor

	# prepare statement to avoid sql injection
	rows = cursor.execute("SELECT * FROM user") # WHERE username = ? AND password = ?", (username, password))
	conn.commit()
	results = rows.fetchall()

	for i in range(len(results)):
		if results[i][0] == password:
			# Get the salt from the database
			salt = results[i][2]
			# Forming the new password with a new password
			password = str(results[i][2]) + password
 
	# compute hash of the password
	digest = hashlib.sha256(password.encode("utf-8")).hexdigest()

	# check if computed digest is equal to stored digest
	if digest == results[i][1].lower():
		return True 
	else: 
		return False

def parse_argument():
	parser = argparse.ArgumentParser()
	
	# command to add a user
	parser.add_argument("-a", help = "add a username (requires -p)", required = False)

	# command to check user credentials
	parser.add_argument("-u", help = "check for a username and a password, (requires -p)", required = False)

	# command for the user password
	parser.add_argument("-p", help = "the username password ", required = True)

	return parser.parse_args()

if __name__ == "__main__":
	
	path = os.path.abspath(os.path.join(os.getcwd(), 'covid_package/database/database.db'))

	open_and_create(path)

	args = parse_argument()

	if args.a and args.p: 
		save_new_username(args.a, args.p)
	elif args.u and args.p: 
		check_for_username(args.u, args.p)
	conn.close()