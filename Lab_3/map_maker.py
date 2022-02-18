"""
Parsing the locations of friends on Twitter and making a map of them.
"""
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import folium
import requests


def get_json_file_from_api(username: str) -> dict:
    """
    Function to get the json file with locations of a certain username
    :param username: str (username)
    :return: json file with locations
    (str -> json)
    """
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMjqZAEAAAAAyG9kB4mUtaz%2BwBOx1qGjAz4qf1'
                         '8%3Dz5SOmNAmwDaPPHYTYPnOsu3IOpjSmvKf2yC7WcoTp9jpE8CSV8'
    }
    user_id = requests.get(f"https://api.twitter.com/2/users/by/username/{username}",
                           headers=headers).json()["data"]["id"]
    return requests.get(f'https://api.twitter.com/2/users/{user_id}/following?user.fields=location',
                        headers=headers).json()["data"]


def location_finder(username: str) -> list:
    """
    Finds locations in the json and makes a list of them.
    :param username: str (username)
    :return: list of locations
    (str -> list)
    """
    data = get_json_file_from_api(username)
    locations, names, ans = [], [], []
    for i in range(len(data)):
        try:
            locations.append(data[i]["location"])
            names.append(data[i]["name"])
        except KeyError:
            i += 1
    for i in range(len(locations)):
        if len(locations[i]) >= 1:
            ans.append([locations[i], names[i]])
    return ans


def coordinate_finder(username: str) -> list:
    """
    Appends the coordinates of the locations.
    :param username: str (path to json file)
    :return: list of tuples with locations and coordinates
    (str -> list)
    """
    data = location_finder(username)
    ans = []
    geolocator = Nominatim(user_agent="PyCharm")
    for i in range(len(data)):
        try:
            location = geolocator.geocode(data[i][0])
            data[i] += (location.latitude, location.longitude)
        except AttributeError or GeocoderUnavailable:
            continue
    for i in data:
        if len(i) == 4:
            ans.append(i)
    return ans


def map_maker(username: str, number_of_friends: int) -> folium:
    """
    Makes a folium map of friends' locations
    :param number_of_friends: int (number of friends to display)
    :param username: str (path to json file)
    :return: folium map
    (str, int -> folium)
    """
    data = coordinate_finder(username)[:int(number_of_friends)]
    m = folium.Map(zoom_start=4)
    for i in data:
        folium.Marker(location=(i[2], i[3]), tooltip=i[0], popup=i[1],
                      icon=folium.Icon(color="red")).add_to(m)
    m.save("Map.html")
    return m.get_root().render()


def main(username, num):
    """
    Main function to start the program.
    """
    return map_maker(username, num)
