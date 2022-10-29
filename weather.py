from time import sleep
from threading import Thread
import requests
from urllib.request import urlopen

def internet_connection():
	try:
		urlopen('http://www.google.com')
		return True
	except:
		return False


# print(internet_connection())

def weather_forecast():

	API_key = '11c0d3dc6093f7442898ee49d2430d20'
	url = 'https://api.openweathermap.org/data/2.5/forecast'
	params = {
		'q': 'Долгопрудный',
		'appid': API_key,
		'units': 'metric',
		'cnt': 2
	}


	while internet_connection() == False:
		Thread(target = weather_forecast).start()
		# response = requests.get(url, params=params)
		yield "Forecast unavailable"
		sleep(60)
		Thread(target = weather_forecast).start()

	response = requests.get(url, params=params)
	information = response.json() 
	Thread(target = weather_forecast).start()
	yield information
	sleep(1800)
	Thread(target = weather_forecast).start()




if __name__ == '__main__':

	while True:
		for i in weather_forecast():
			if i == "Forecast unavailable":
				print(i)
				print()
			else:
				print('Прогноз погоды на текущий момент времени:')
				print('Температура', i['list'][0]['main']['temp'])
				print('Ощущается как', i['list'][0]['main']['feels_like'])
				print('Влажность', i['list'][0]['main']['humidity'])
				print('Тип осадков', i['list'][0]['weather'][0]['main'])
				print('Сила осадков', i['list'][0]['weather'][0]['description'])
				print('Скорость ветра', i['list'][0]['wind']['speed'])
				print('Направление ветра в градусах', i['list'][0]['wind']['deg'])
				print()
				print('Прогноз погоды через 3 часа:')
				print('Температура', i['list'][1]['main']['temp'])
				print('Ощущается как', i['list'][1]['main']['feels_like'])
				print('Влажность', i['list'][1]['main']['humidity'])
				print('Тип осадков', i['list'][1]['weather'][0]['main'])
				print('Сила осадков', i['list'][1]['weather'][0]['description'])
				print('Скорость ветра', i['list'][1]['wind']['speed'])
				print('Направление ветра в градусах', i['list'][1]['wind']['deg'])
				print()
				print()

