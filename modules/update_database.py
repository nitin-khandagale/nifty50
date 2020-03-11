from database_queries import update_database, get_db_data
import mysql.connector

def update_fundamentals():
	query = """INSERT INTO dummy.pistol(high, low, opened, closed)
				VALUES (4794.23, 1199.78, 7777.78, 7888.90)"""

	update_database(query, "Fundamentals")


def update_msf():	
	query = """
	UPDATE dummy.pistol
	SET MSF = ( @msf := CASE WHEN msf IS NULL
	THEN (closed - @msf) * 0.33 + @msf
	ELSE msf
	END )
	ORDER BY Sr;"""

	update_database(query, "MSF")

def update_range():
	for i in range(1,10):
		query = """UPDATE dummy.pistol
					SET rangee = high - low
					WHERE Sr={}""".format(i)

		update_database(query, "Range")

# JGD = ""
# JWD = ""

def update_directors_pattern():
	for i in range(2, 10):
		
		query = """SELECT JGD, JDW from martha.nifty_excel_data_all
						where Sr = {}""".format(i)

		query_2 = """SELECT JDW FROM martha.nifty_excel_data_all
										WHERE Sr = {}""".format(i-1)

		result = get_db_data('localhost', 'root', 'root', 'martha', query, 1)

		todays_jgd = result[0]
		todays_jwd = result[1]
		yesterdays_jwd = db_fetch_data('localhost', 'root', 'root', 'martha', query_2, 1)	
		
		try:
			pattern = ''
			if todays_jgd > yesterdays_jwd[0] and todays_jwd > yesterdays_jwd[0]:
				pattern = '2 + 2'

			if todays_jgd > yesterdays_jwd[0] and todays_jwd < yesterdays_jwd[0]:
				pattern = '2 + 1'

			if todays_jgd < yesterdays_jwd[0] and todays_jwd < yesterdays_jwd[0]:
				pattern = '3 + 1'

			query_3 = """UPDATE martha.nifty_excel_data_all
							SET directors_pattern = '{}'
							WHERE Sr = {} AND directors_pattern IS NULL""".format(pattern, i)

			update_database(query_3, "Directors Pattern")
		
		except Exception as e:
			print("Error in assigning directors pattern : {}".format(e))


# update_fundamentals()
# update_msf()
# update_range()
# update_directors_pattern()