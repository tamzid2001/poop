from flask import Flask, render_template,request
import weatherstuff 

weather = Flask(__name__)



@weather.route('/', methods = ['POST','GET'])
def get_weather():
    if request.method == 'GET':
        return render_template('webweather.html')
    else:
        formx = request.form
        city = formx['cityx']
    a = weatherstuff.city(city)
    t = a['main']['temp']
    return render_template('webweather.html', temp = t)



if __name__ == '__main__':
    weather.debug = True
    weather.run(host = '0.0.0.0')
