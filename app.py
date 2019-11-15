from flask import Flask, request, render_template
import requests
#https://docs.python.org/3/library/venv.html
#py -m venv <yourfolder>
# source bin/activate

app = Flask(__name__)
app.debug = True

@app.route("/")
def search():
    ''' Input city name '''
    return render_template("search.html")

@app.route("/weather_results")
def results():
    city = request.args.get("city")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ae2660cbfb15ae919e944f013ed49449"
    res = requests.get(url)
    json = res.json()

    weather = json["weather"][0]["main"]
    string = f"There is {weather} right now in {city}!"
    return render_template("results.html", string=string)




if __name__ == '__main__':
    app.run()
