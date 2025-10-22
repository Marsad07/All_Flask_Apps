from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Marsad's Flask App 1!, to look at the about page, add /about on the url "

@app.route('/about')
def about():
    return ("Hi there, my names Marsad and i'm a student who wants to "
            "pursue a career in the path of Software Engineering, while"
            "your looking through my github, you will see a variety of apps"
            "made using flask, from easy simple ones to more advanced and complex "
            "apps. ")

if __name__ == '__main__':
    app.run(debug=True)