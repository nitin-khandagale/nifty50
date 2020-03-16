import datetime
from datetime import datetime, timedelta
from database_queries import update_database, get_db_data
import random
import string


def data_bet_two_dates():
	start = datetime(2008, 8, 15).date()
	end = datetime(2010, 8, 22).date()
	delta = end - start

	for i in range(delta.days + 1):
		fucks = start + timedelta(days=i)
		print("{}   --->   {}".format(fucks, fucks.weekday()))

data_bet_two_dates()

week_con = 7
for i in range(0, 7):
	today = datetime.today().date() 
	over_days = week_con + today.weekday()
	last_mon = today - timedelta(days=over_days)
	last_week = last_mon + timedelta(days=i)

	query = """SELECT codes from martha.orders
				WHERE datee = '{}'""".format(last_week)
	codes = get_db_data(query, 1, "get_codes")
	print(last_week)
	print(codes)

current_weekday = datetime.today().weekday() + 3
for i in range(0, abs(current_weekday)):
	today = datetime.today().date() + timedelta(days=4)
	mon = today - timedelta(days=abs(current_weekday))
	week_data = mon + timedelta(days=i)
	
	query = """SELECT codes from martha.orders
				WHERE datee = '{}'""".format(week_data)

	codes = get_db_data(query, 1, "Dates")
	print(week_data)
	print(codes)

