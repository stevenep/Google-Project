from flask import Flask, render_template, request
import requests


app = Flask(__name__)
# api_key = 'A34F48&v=1'
# https://api.adoptapet.com/search/pets_at_shelters?key=A34F48&v=1&output=xml&shelter_id=2342&shelter_id=17293&shelter_id=8323


@app.route('/')
def index():
    response = requests.get(f'https://www.freetogame.com/api/games')
    data = response.json()
    return render_template('index.html', data = data)
    print(data)

# @app.route('/message', methods=['POST'])
# def post_message():
    
#     message = request.form['message']
#     return render_template('result.html', data = data)

@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['platform']
    category = request.form['category']
    release_date = request.form['year']
    response = requests.get(f' https://www.freetogame.com/api/games?platform={message}&category={category}&sort-by={release_date}')
    data = response.json()
    return render_template('result.html', data = data)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')