from model.Date import Date

def response_parser(response):
    response_json = response.json()
    currency = response_json['moneda']
    type_currency = response_json['casa']
    sellValue = float(response_json['venta'])
    buyValue = float(response_json['compra'])
    date = response_json['fechaActualizacion'].split("T")[0]
    hour = response_json['fechaActualizacion'].split("T")[1].split(".")[0]
    date_obj = Date(date, hour)
    return currency, type_currency, sellValue, buyValue, date_obj