from django.shortcuts import render

def home(request):
    import requests
    import json
    #Price API
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,LTC,XLM,ADA,USDT,MIOTA,TRX,EOSXRP&tsyms=CAD")
    price = json.loads(price_request.content)


    #News API
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    return render(request, 'prices.html', {})