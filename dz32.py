import datetime
import calendar


date = datetime.datetime.now()
print(f"Текущая дата: {date}")


weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print(f"Текущий день недели: {weekdays[date.weekday()]}")


year = date.year
if calendar.isleap(year):
    print(f"{year} - високосный год.")
else:
    print(f"{year} - не високосный год.")


date_request = input("Введите дату в формате 'год-месяц-день': ")
now_date = datetime.datetime.strptime(date_request, "%Y-%m-%d")
difference = date - now_date
seconds = difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print(f"Осталось: {abs(difference.days)} дней, {hours} часов, {minutes} минут.")