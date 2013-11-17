
import requests
import xml.etree.ElementTree as ET


class InvalidAppIdException(Exception):
    pass


class InvalidWoeIdException(Exception):
    pass


class InvalidPlaceException(Exception):
    pass


class Wyther(object):

    Y_GEOPLANET_API_URL = "http://where.yahooapis.com/v1/places.q"
    Y_WEATHER_API_URL = "http://weather.yahooapis.com/forecastrss"
    ROOT_INDEX = 0
    ITEM_INDEX = 12
    YWEATHER_CONDITION_INDEX = 5

    def __init__(self,app_id):
        self.app_id = app_id

    def get_place_woeid(self, place):
        """Gets the WOEID of a place

        Args:
            place (tuple): a tuple of city and country or city and state.
        Returns:
            str. The WOEID
        Raises:
            InvalidAppIdException, InvalidPlaceException"""
        x = requests.get(self.Y_GEOPLANET_API_URL+'('+'%20'.join(place)+')',params={'appid':self.app_id})
        root = ET.fromstring(x.text)
        try:
            if root[self.ROOT_INDEX].text == '400 Bad Request':
                raise InvalidAppIdException()
            return root[self.ROOT_INDEX][self.ROOT_INDEX].text
        except IndexError:
            raise InvalidPlaceException()

    def by_woeid(self,woeid,units='f'):
        """Gets the weather of a place by woeid

        Args:
            woeid (int): the WOEID of the place.
            units (str): the units::
                f -- fahrenheit
                c -- celsius
        Returns:
            float. The weather
        Raises:
            InvalidWoeIdException"""
        x = requests.get(self.Y_WEATHER_API_URL,params={'w': woeid, 'u': units})
        root = ET.fromstring(x.text)
        if root[self.ROOT_INDEX][self.ROOT_INDEX].text == 'Yahoo! Weather - Error':
            raise InvalidWoeIdException()
        return float(root[self.ROOT_INDEX][self.ITEM_INDEX][self.YWEATHER_CONDITION_INDEX].get('temp'))

    def by_place(self,place,units='f'):
        """Gets the weather of a place by city and country or city and state

        Args:
            place (tuple): a tuple of city and country or city and state.
            units (str): the units::
                f -- fahrenheit
                c -- celsius
        Returns:
            float. The weather"""
        return self.by_woeid(self.get_place_woeid(place),units)