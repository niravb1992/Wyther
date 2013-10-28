
Wyther
================
A simple Python wrapper class for Yahoo Weather API

Prerequisites
=================
1. Python requests module must be installed (http://www.python-requests.org/en/latest/)
2. You must register at http://developer.yahoo.com/wsregapp to get an appid. 

Usage
=================

Example:

```
from wyther.Wyther import Wyther
APP_ID = 'YOUR APP ID'
w = Wyther(APP_ID)
print w.get_weather(('atlanta','us'))
```
