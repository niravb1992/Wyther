import requests
import xml.etree.ElementTree as ET


class InvalidAppIdException(Exception):
    """
    The exception thrown on an invalid app id
    """
    pass


class InvalidWoeIdException(Exception):
    """
    The exception thrown on an invalid woeid
    """
    pass


class InvalidPlaceException(Exception):
    """
    The exception thrown on an invalid place
    """
    pass


class Wyther(object):
    """
    The weather of a place using Yahoo Weather API
    """
    Y_GEOPLANET_API_URL = "http://where.yahooapis.com/v1/places.q"
    Y_WEATHER_API_URL = "http://weather.yahooapis.com/forecastrss"
    ROOT_INDEX = 0
    ITEM_INDEX = 12
    YWEATHER_CONDITION_INDEX = 5

    def __init__(self,app_id):
        """
        Creates a new Wyther object

        @type app_id: str
        @param app_id: the app id obtained from a yahoo developers account
        """
        self.app_id = app_id

    def get_place_woeid(self, place):
        """
        Returns the WOEID of a place

        @type place: tuple
        @param place: a tuple of city and country or city and state
        @rtype: str
        @return: the WOEID of place
        @raise InvalidAppIdException: If the app id provided is invalid
        @raise InvalidPlaceException: If the place tuple provided is invalid
        """
        x = requests.get(self.Y_GEOPLANET_API_URL+'('+'%20'.join(place)+')',params={'appid':self.app_id})
        root = ET.fromstring(x.text)
        try:
            if root[self.ROOT_INDEX].text == '400 Bad Request':
                raise InvalidAppIdException()
            return root[self.ROOT_INDEX][self.ROOT_INDEX].text
        except IndexError:
            raise InvalidPlaceException()

    def by_woeid(self,woeid,units='f'):
        """
        Returns the weather of a place by woeid

        @type woeid: int
        @param woeid: the woeid of a place
        @type units: str
        @param units: the units of the weather
        @rtype: float
        @return: the weather of the place
        @raise InvalidWoeIdException: If the woeid provided is invalid
        """
        x = requests.get(self.Y_WEATHER_API_URL,params={'w': woeid, 'u': units})
        root = ET.fromstring(x.text)
        if root[self.ROOT_INDEX][self.ROOT_INDEX].text == 'Yahoo! Weather - Error':
            raise InvalidWoeIdException()
        return float(root[self.ROOT_INDEX][self.ITEM_INDEX][self.YWEATHER_CONDITION_INDEX].get('temp'))

    def by_place(self,place,units='f'):
        """
        Returns the weather of a place by woeid

        @type place: tuple
        @param place: a tuple of city and country or city and state
        @type units: str
        @param units: the units of the weather
        @rtype: float
        @return: the weather of the place
        """
        return self.by_woeid(self.get_place_woeid(place),units)
