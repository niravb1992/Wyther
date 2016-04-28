import requests

class Wyther(object):
    """
    A class to get the temperature of a place using Yahoo Weather API
    """
    Y_WEATHER_API_URL = "https://query.yahooapis.com/v1/public/yql"

    def __init__(self):
        """
        Creates a new Wyther object
        """
        pass

    def by_woeid(self,woeid,units='f'):
        """
        Returns the temperature of a place by woeid

        @type woeid: int
        @param woeid: the woeid of a place
        @type units: str
        @param units: the units of the weather
        @rtype: float
        @return: the weather of the place
        @raise InvalidWoeIdException: If the woeid provided is invalid
        """
        response = requests.get(self.Y_WEATHER_API_URL, params={
        'q':'select item.condition from weather.forecast where u="'+units+'" and woeid = '+str(woeid),
        'format':'json'
        })
        return response.json()['query']['results']['channel']['item']['condition']['temp']

    def by_place(self,place,units='f'):
        """
        Returns the temperature of a place

        @type place: tuple
        @param place: a tuple of city and country or city and state
        @type units: str
        @param units: the units of the weather
        @rtype: float
        @return: the weather of the place
        """
        response = requests.get(self.Y_WEATHER_API_URL, params={
        'q':'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text="'+','.join(place)+'") and u="'+units+'"',
        'format':'json'
        })
        return response.json()['query']['results']['channel']['item']['condition']['temp']
