from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/fetch-floor-price', methods=['GET'])
def fetch_floor_price():
    try:
        magic_eden_api_url = 'https://api-mainnet.magiceden.dev/v2/collections/juic3dnfts/stats'
        dex_screener_api_url = 'https://api.dexscreener.com/latest/dex/tokens/83v8ipyzihdejddy8rdzddyznyutxngz69lgo9kt5d6d'

        me_response = requests.get(magic_eden_api_url)
        me_data = me_response.json()

        ds_response = requests.get(dex_screener_api_url)
        ds_data = ds_response.json()

        floor_price_sol = me_data['stats']['floorPrice'] / 1_000_000_000
        sol_price_usd = ds_data['price']

        return jsonify({
            'floorPriceSol': floor_price_sol,
            'solPriceUsd': sol_price_usd
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)