from flask import Flask, render_template
import xxx 

xxx2 = Flask(__name__)

@xxx2.route('/')
def xx():
    x = xxx.city("Paris")
    return render_template('xxxx.html', temp = x)



if __name__ == '__main__':
    xxx2.debug = True
    xxx2.run()
