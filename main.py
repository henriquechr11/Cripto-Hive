from numpy import double
import requests
import os
import pprint
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
import pandas as pd
from flask import Flask , render_template 


load_dotenv(override=True)

cg = CoinGeckoAPI()



# utilisa o flask para usar html e css
app = Flask(__name__)

# pega a coinlist e transforma em lista
# coinlist = cg.get_coins_list()
# coindataframe = pd.DataFrame.from_dict(coinlist).sort_values(by='id').reset_index(drop=True)

cotacoes= ['usd', 'brl', 'link']
# counterCurrencies = cg.get_supported_vs_currencies()
# print(counterCurrencies)
coins = ['bitcoin', 'ethereum', 'dogecoin', 'dopex']

# printa os preços simples das criptomoedas
# simplePriceRequest = cg.get_price(ids=coins, vs_currencies=cotacoes)
# pprint.pprint(simplePriceRequest)

# printa as informações mais completas das criptomoedas
# complexPriceRequest = cg.get_price(ids=coins, vs_currencies=cotacoes , include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
# pprint.pprint(complexPriceRequest)


# pricebt_raw = cg.get_price(ids='bitcoin', vs_currencies='usd' , include_24hr_change = True)
#     bt_price = pricebt_raw.get('bitcoin', {}).get('usd')
#     bt_change = pricebt_raw.get('bitcoin', {}).get('usd_24h_change')
#     if isinstance(bt_price, (int, float)) and isinstance(bt_change, (int, float)):
#         pricebt = f"USD({int(round(bt_price))},00) | 24h: {bt_change:.2f}%"
#     else:
#         pricebt = "USD(0,00) | 24h: 0,00%"



@app.route("/")
def home():






    pricebt_raw = cg.get_price(ids='bitcoin', vs_currencies='usd' , include_24hr_change = True)
    bt_price = pricebt_raw.get('bitcoin', {}).get('usd')
    bt_change = pricebt_raw.get('bitcoin', {}).get('usd_24h_change')
    if isinstance(bt_price, (int, float)) and isinstance(bt_change, (int, float)):
        pricebt = f"USD {float(bt_price)}  |  {bt_change:.2f}%"
    else:
        pricebt = "USD(0,00) | 24h: 0,00%"


    pricedg_raw = cg.get_price(ids='dogecoin', vs_currencies='usd' , include_24hr_change = True)
    dg_price = pricedg_raw.get('dogecoin', {}).get('usd')
    dg_change = pricedg_raw.get('dogecoin', {}).get('usd_24h_change')
    if isinstance(dg_price, (int, float)) and isinstance(dg_change, (int, float)):
        pricedg = f"USD {float(dg_price)} |  {dg_change:.2f}%"
    else:
        pricedg = "USD(0,0aa) | 24h: 0,00%"


    priceet_raw = cg.get_price(ids='ethereum', vs_currencies='usd' , include_24hr_change = True)
    et_price = priceet_raw.get('ethereum', {}).get('usd')
    et_change = priceet_raw.get('ethereum', {}).get('usd_24h_change')
    if isinstance(et_price, (int, float)) and isinstance(et_change, (int, float)):
        priceet = f"USD {float(et_price)}  |  {et_change:.2f}%"
    else:
        pricedg = "USD(0,00) | 24h: 0,00%"



    pricedpx_raw = cg.get_price(ids='dopex', vs_currencies='usd' , include_24hr_change = True)
    px_price = pricedpx_raw.get('dopex', {}).get('usd')
    px_change = pricedpx_raw.get('dopex', {}).get('usd_24h_change')
    if isinstance(px_price, (int, float)) and isinstance(px_change, (int, float)):
        pricedopx = f"USD {float(px_price)}  |  {px_change:.2f}%"
    else:
        pricedopx = "USD(0,00) | 24h: 0,00%"


    


    return render_template("index.html" , precobit=pricebt, pricedog= pricedg, priceeth=priceet,  pricedpx=pricedopx)



if __name__ == "__main__":
    app.run()




