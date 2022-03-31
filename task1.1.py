duration = int(input("Введите количество секунд: "))
minute = 60
hour = 3600
day = 86400
week = 604800
if duration < minute :
    print (duration, "сек")
elif duration >= minute and duration < hour :
    our_minute = duration // minute
    our_seconds = duration % minute
    print(our_minute, "минут", our_seconds, "секунд")
elif duration >= hour and duration <= day :
    our_hours = duration // hour
    our_minute = duration % minute
    our_seconds = duration % minute
    print(our_hours, "часов", our_minute, "минут", our_seconds, "секунд")
elif duration >= day and duration <= week :
    our_day = duration // day
    duration = duration % day
    our_hours = duration // hour
    duration = duration % hour
    our_minute = duration // minute
    our_seconds = duration % minute
    print(our_day, "дней", our_hours, "часов", our_minute, "минут", our_seconds, "секунд")