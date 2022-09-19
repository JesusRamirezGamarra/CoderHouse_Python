from datetime import datetime 
#import datetime
today_and_now = datetime.now()  # Fecha y hora Actual

print(today_and_now)
print(today_and_now.year)
print(today_and_now.month)
print(today_and_now.day)

print(today_and_now.hour)
print(today_and_now.minute)
print(today_and_now.second)
print(today_and_now.microsecond)


# print(today_and_now.MINYEAR)

mi_fecha = datetime(2018,12,9,9,15,8)
print(mi_fecha)

today_and_now_format = today_and_now.strftime("%A %d %B %Y %I: %M")
print(today_and_now_format)
