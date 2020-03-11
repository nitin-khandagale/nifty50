from db_connection import get_db_connection
import mysql.connector

mydb = mysql.connector.connect(
			host='localhost',
			user='root',
			password='root',
			database='dummy'
			)
		
cursor = mydb.cursor()

def update_database(Query, Description):
	
	# cursor = get_db_connection("localhost", "root", "root", "martha")
	try:
		sql_query = Query
		print("Executing {}".format(Description))
		cursor.execute(sql_query)
		mydb.commit()
		print("{} query updated !".format(Description))
		print("\n")
	except Exception as e:
		print("Error while updating {} query !".format(Description))
		print("Source and location : modules >> database_queres >> update_database()")
		print("Error : {}".format(e))
		print("\n")


def get_db_data(Query, fetch_type, Description):
	# cursor = get_db_connection("localhost", "root", "root", "martha")
	try:
		sql_query = Query

		print("Getting data for {} query !".format(Description))
		cursor.execute(sql_query)
		print("Query for {} executed !".format(Description))

		if fetch_type == 1:
			fetch_result = cursor.fetchone()
		else:
			fetch_result = cursor.fetchall()
		# mydb.commit()

		return fetch_result
	except Exception as e:
		print("Error while executing {} query !".format(Description))
		print("Source location : db_fetch_data from db_connection file")
		print("Error : {}".format(e))
		print("\n")


# def store_msf():
# 	try:
# 		query = """UPDATE martha.nifty_excel_data_all
# 								SET MSF = ( @msf := CASE WHEN msf IS NULL
# 								THEN (closed - @msf) * 0.33 + @msf
# 								ELSE msf
# 								END )
# 								ORDER BY Sr;"""

# 		db_connection("localhost", "root", "root", "martha", query)
# 	except Exception as e:
# 		print("Error while getting msf !")
# 		print("Source location : modules >> arithmatic_modules >> get_msf()")
# 		print("ERROR : {}".format(e))
