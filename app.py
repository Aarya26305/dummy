from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "75bf01db9a964f67a7e145158260705"

@app.route('/', methods=['GET', 'POST'])
def home():

    weather = None
    error = None

    if request.method == 'POST':

        city = request.form['city']

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)

        data = response.json()

        if "error" in data:

            error = "City not found!"

        else:

            weather = {
                "city": data['location']['name'],
                "country": data['location']['country'],
                "temperature": data['current']['temp_c'],
                "humidity": data['current']['humidity'],
                "description": data['current']['condition']['text'],
                "wind": data['current']['wind_kph']
            }

    return render_template(
        'index.html',
        weather=weather,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)