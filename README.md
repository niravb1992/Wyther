About
================
wyther is a Python module to get the temperature of a place using [Yahoo Weather API](https://developer.yahoo.com/weather/)

Installation
=================

Download the source code, extract it, cd into the Wyther directory, and run:

````
python setup.py install
````

Usage
=================
Get temperature by place (a tuple/string of city and country or city and state)

	from wyther.Wyther import Wyther
	wyther = Wyther()
	print wyther.by_place(('atlanta','us'))

The above example gets the temperature in Fahrenheit. To get the temperature in Celsius

	wyther.by_place(('atlanta','us'),'c')

Get temperature by woeid

	wyther.by_woeid(2442047) # gets the temperature in fahrenheit of los angeles
