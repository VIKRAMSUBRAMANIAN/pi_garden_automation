#TODO display the coordinates using geocoding API
#TODO soil moisture data from Agro API
import requests, json, time

#geocoding api key -->  'AIzaSyD8mX_8hCA8YJEP8nWvkCM4qmUvA8tnB1E'
# api request format: https://maps.googleapis.com/maps/api/geocode/json?paramet$


def city_name = input("Enter name of place")
    #code to generate the url
    API_KEY = "ac355a3f4acc38795d2efc933771f5f7"
    domain = "http://api.openweathermap.org/data/2.5/weather?q="
    url = domain + city_name + "&APPID=" + API_KEY

    #Geocoding
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    KEY = "&key=AIzaSyD8mX_8hCA8YJEP8nWvkCM4qmUvA8tnB1E"
    words = city_name.split()
                               [ Read 80 lines ]
^G Get Help  ^O Write Out ^W Where Is  ^K Cut Text  ^J Justify   ^C Cur Pos
^X Exit      ^R Read File ^\ Replace   ^U Uncut Text^T To Linter ^_ Go To Line
