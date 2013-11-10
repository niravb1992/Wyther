Wyther
================
A simple Python wrapper to the Yahoo Weather API

Prerequisites
=================
1. Register at http://developer.yahoo.com/wsregapp to get an appid.
2. Install requests module (http://www.python-requests.org/en/latest/)

Installation
=================

From the Wyther directory, run:

	python setup.py install

Usage
=================
Get weather by place (a tuple of city and country or city and state)


	from wyther.Wyther import Wyther
	APP_ID = 'YOUR APP ID'
	wyther = Wyther(APP_ID)
	print wyther.by_place(('atlanta','us'))

The above example gets the weather in Fahrenheit. To get the weather in Celsius

	wyther.by_place(('atlanta','us'),'c')

Get weather by woeid

	wyther.by_woeid(2442047) # gets the weather in fahrenheit of los angeles
