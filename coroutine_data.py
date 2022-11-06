import numpy as np

def my_coroutine(func):
	def inner(*args, **kwargs):
		f = func(*args, **kwargs)
		f.send(None)
		return f
	return inner


@my_coroutine
def data_processing():
	quantity = 0
	data = []
	information = None

	while True:
		try:
			x = yield information
		except StopIteration:
			print('Done')
			break
		else:
			quantity += 1
			data.append(x)
			mean = round(np.mean(data), 2)
			variance = round(np.var(data), 2)
			information = {
			'Среднее значение': mean,
			'Дисперсия': variance,
			'Количество элементов': quantity
			}


#Пример работы
g = data_processing()
print(g.send(5))
print(g.send(10))

