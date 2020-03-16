import mysql.connector

def get_db_connection(Hostname, User, Pw, Db):
	try:
		mydb = mysql.connector.connect(
			host=Hostname,
			user=User,
			password=Pw,
			database=Db
			)
		
		cursor = mydb.cursor()
		return cursor
	except Exception as e:
		print("Error while connecting to database !")
		print("Source : modules >> db_connection >> db_connection()")
		print("ERROR : {}".format(e))

