import mysql.connector
from database_connection import db_connection

def get_msf():
	try:
		query = """UPDATE martha.nifty_excel_data_all
								SET MSF = ( @msf := CASE WHEN msf IS NULL
								THEN (closed - @msf) * 0.33 + @msf
								ELSE msf
								END )
								ORDER BY Sr;"""

		db_connection("localhost", "root", "root", "martha", query)
	except Exception as e:
		print("Error while getting msf !")
		print("Source location : modules >> arithmatic_modules >> get_msf()")
		print("ERROR : {}".format(e))