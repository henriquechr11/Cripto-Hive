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
        pricebt = f"{float(bt_price):,.2f}".replace(',', ' ')
        bt_change_formatted = bt_change
        bt_change_class = 'positive' if bt_change > 0 else 'negative' if bt_change < 0 else ''
    else:
        pricebt = "0.00"
        bt_change_formatted = 0.0
        bt_change_class = ''


    pricedg_raw = cg.get_price(ids='dogecoin', vs_currencies='usd' , include_24hr_change = True)
    dg_price = pricedg_raw.get('dogecoin', {}).get('usd')
    dg_change = pricedg_raw.get('dogecoin', {}).get('usd_24h_change')
    if isinstance(dg_price, (int, float)) and isinstance(dg_change, (int, float)):
        pricedg = f"{float(dg_price):,.2f}".replace(',', ' ')
        dg_change_formatted = dg_change
        dg_change_class = 'positive' if dg_change > 0 else 'negative' if dg_change < 0 else ''
    else:
        pricedg = "0.00"
        dg_change_formatted = 0.0
        dg_change_class = ''


    priceet_raw = cg.get_price(ids='ethereum', vs_currencies='usd' , include_24hr_change = True)
    et_price = priceet_raw.get('ethereum', {}).get('usd')
    et_change = priceet_raw.get('ethereum', {}).get('usd_24h_change')
    if isinstance(et_price, (int, float)) and isinstance(et_change, (int, float)):
        priceet = f"{float(et_price):,.2f}".replace(',', ' ')
        et_change_formatted = et_change
        et_change_class = 'positive' if et_change > 0 else 'negative' if et_change < 0 else ''
    else:
        priceet = "0.00"
        et_change_formatted = 0.0
        et_change_class = ''



    pricedpx_raw = cg.get_price(ids='dopex', vs_currencies='usd' , include_24hr_change = True)
    px_price = pricedpx_raw.get('dopex', {}).get('usd')
    px_change = pricedpx_raw.get('dopex', {}).get('usd_24h_change')
    if isinstance(px_price, (int, float)) and isinstance(px_change, (int, float)):
        pricedopx = f"{float(px_price):,.2f}".replace(',', ' ')
        px_change_formatted = px_change
        px_change_class = 'positive' if px_change > 0 else 'negative' if px_change < 0 else ''
    else:
        pricedopx = "0.00"
        px_change_formatted = 0.0
        px_change_class = ''


    


    return render_template("index.html" , 
                         precobit=pricebt, changebit=bt_change_formatted, changebit_class=bt_change_class,
                         pricedog=pricedg, changedog=dg_change_formatted, changedog_class=dg_change_class,
                         priceeth=priceet, changeeth=et_change_formatted, changeeth_class=et_change_class,
                         pricedpx=pricedopx, changedpx=px_change_formatted, changedpx_class=px_change_class)

        

if __name__ == "__main__":
    app.run()



    