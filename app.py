from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI
import pandas as pd

app = Flask(__name__)

# Chave API (embora a CoinGecko não exija)
API_KEY = "CG-fKjvzkiSgqLTtb3vdLuJ6SeZ"  # Substitua se necessário

@app.route('/')
def index():
    # Inicializando a API
    cg = CoinGeckoAPI()
    
    # Obtendo as 100 principais criptomoedas
    top_coins = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page=100, page=1)
    
    # Criando DataFrame
    df = pd.DataFrame(top_coins)
    
    # Filtrando as altcoins (excluindo Bitcoin e Ethereum)
    altcoins = df[(df['id'] != 'bitcoin') & (df['id'] != 'ethereum')]
    
    # Separando as 10 maiores altcoins
    top_altcoins = altcoins.nlargest(10, 'market_cap')
    
    # Separando as 10 altcoins mais baratas
    cheap_altcoins = altcoins.nsmallest(10, 'current_price')
    
    # Filtrando as moedas que tiveram valorização nas últimas 24 horas
    gainers_24h = df[df['price_change_percentage_24h'] > 0]
    
    return render_template('index.html', 
                           top_altcoins=top_altcoins.to_dict(orient='records'),
                           cheap_altcoins=cheap_altcoins.to_dict(orient='records'),
                           gainers_24h=gainers_24h.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)