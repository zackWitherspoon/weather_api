import unittest
import weather_api

class TestWeatherApi(unittest.TestCase):

	def test_buildString(self):
		result = weather_api.buildString(12, 23, 'HOWDY-YALL')
		self.assertEqual(result, 'https://api.openweathermap.org/data/2.5/onecall?lat=12&lon=23&exclude=hourly,minutely,alerts&units=imperial&appid=HOWDY-YALL')

	def test_ping(self):
		result = weather_api.ping()
		self.assertEqual(result, 401)

if __name__ == '__main__':
	unittest.main()