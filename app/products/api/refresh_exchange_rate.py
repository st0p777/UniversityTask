from py_exchangeratesapi import Api
from app.settings import exchange_rates_api_key

from products.models import Exchanges


def connect():
    try:
        return Api(exchange_rates_api_key)
    except:
        return


def update():
    print("exchange")
    api = connect()
    print(api)
    if api:
        usd = api.get_rate('USD', 'RUB')
        eur = api.get_rate('EUR', 'RUB')
        exchange_object = Exchanges.objects.all().first()
        if exchange_object:
            exchange_object.usd = usd
            exchange_object.eur = eur
            exchange_object.save()
        else:
            Exchanges.objects.create(usd=usd, eur=eur)


