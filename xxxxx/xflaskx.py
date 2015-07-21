from flask import Flask, render_template
import weatherstuff 

weather = Flask(__name__)

@weather.route('/weather')
def get_weather():
    a = weatherstuff.city("Paris")
    return render_template('webweather.html', temp = a)



if __name__ == '__main__':
    weather.debug = True
    weather.run()
