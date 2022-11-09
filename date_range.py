from datetime import datetime, timedelta

def date_range(start, stop, step):

	while start < stop:
		yield start
		start += step

#Данные должны подаваться в генератор в формате даты. 
#Для этого используется библиотека datetime. 
#Шаг генератора задаем через timedelta.
#Эта функция принимает параметры days, hours и тд. 
#Для того, чтобы задать шаг в год/месяц, это время надо перевести в количество дней.
a = datetime(year=2022, month=10, day=24, hour=22, minute=37)
b = datetime(year=2022, month=10, day=27, hour=22, minute=37)
c = timedelta(days=1, hours=0, minutes=0)

for i in date_range(a, b, c):
	print(i)







