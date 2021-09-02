# dz_1_1. Output of information about the time interval depending on its duration in seconds
interval = int(input('Please enter the time interval in seconds: '))
if interval < 60:
    print(interval,'sec')
elif interval < 3600:
    interval_min = interval // 60
    interval_sec = interval % 60
    print(interval_min,'min',interval_sec,'sec')
elif interval < 86400:
    interval_hrs = interval // 3600
    interval_min = (interval - interval_hrs * 3600) // 60
    interval_sec = (interval - interval_hrs * 3600) % 60
    print(interval_hrs,'hours', interval_min, 'min', interval_sec,'sec')
else:
   interval_days = interval // 86400
   interval_hrs = (interval - interval_days * 86400) // 3600
   interval_min = (interval - interval_days * 86400 - interval_hrs * 3600) // 60
   interval_sec = (interval - interval_days * 86400 - interval_hrs * 3600) % 60
   print(interval_days, 'days', interval_hrs,'hours', interval_min, 'min', interval_sec,'sec')
