import datetime
from datetime import datetime, timedelta
from database_queries import update_database
import random
import string





week_con = 7
for i in range(0, 7):
	today = datetime.today().date() - timedelta(days=1)
	over_days = week_con + today.weekday()
	last_mon = today - timedelta(days=over_days)
	last_week = last_mon + timedelta(days=i)
	print(last_week)

current_weekday = datetime.today().weekday() #+ 3
for i in range(0, current_weekday):

	today = datetime.today().date() #+ timedelta(days=3)

	mon = today - timedelta(days=current_weekday)

	week_data = mon + timedelta(days=i)

	print(week_data)





