# from datetime import datetime
# from datetime import date
import datetime
# current_date = datetime.now()
# print(current_date.day,current_date.month, current_date.year)
#
# current_date2 = date.today()
# print(current_date2, current_date2.day,current_date2.month, current_date2.year)

# current_date3 = datetime.datetime.now()
# current_date3.strftime('X%d/X%m/%Y')
# print(current_date3.strftime)
todayDate = datetime.date.today().strftime("%m %d %Y")
print(todayDate)
