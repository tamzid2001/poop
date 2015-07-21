import urllib2 as urllib
import json
def city(city):
    u = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city)
    t = u.read()
    return json.loads(t)                

    
