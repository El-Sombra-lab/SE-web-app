from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Replace 'YOUR_POLYGON_API_KEY' with your actual Polygon.io API key
    polygon_api_key = 'Ehsps9FWIU8xzdI4uv02lE7seRF0fLVZ'
    # Replace 'AAPL' with the symbol of the company you want to track
    stock_symbol = 'AAPL'

    # Make a request to Polygon.io for real-time stock data
    response = requests.get(
        f'https://api.polygon.io/v1/last/stocks/{stock_symbol}?apiKey={polygon_api_key}'
    )

    if response.status_code == 200:
        stock_data = response.json()
        return render_template('index.html', stock_data=stock_data)
    else:
        return 'Error fetching stock data'

if __name__ == '__main__':
    app.run(debug=True)
