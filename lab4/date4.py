from datetime import timedelta,datetime,date
today=datetime.today()
random = datetime(2022, 3, 2, 12, 30, 10)
ans=(today.day - random.day)*86400+(today.hour- random.hour)*3600 + (today.minute - random.minute)*60 + (today.second-random.second)
print(ans)
