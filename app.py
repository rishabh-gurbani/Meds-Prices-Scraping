from flask import Flask, request, jsonify
from Tata import searchTata
from PharmEasy import searchPE
from Apollo_webscraper import searchApollo

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/prices', methods=['POST'])
def get_prices():
    medicine = request.form.get('med')
    results = [searchApollo(medicine), searchPE(medicine), searchTata(medicine)]

    return jsonify({'Apollo': results[0],
                    'PharmEasy': results[1],
                    'Tata': results[2]
                    })


if __name__ == '__main__':
    app.run()
