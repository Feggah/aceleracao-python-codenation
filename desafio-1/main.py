from datetime import datetime
from operator import itemgetter
import pytz

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

SECONDS = 60
MINUTES = 60
SWITCH_TAX_NIGHT = 22 * SECONDS * MINUTES
SWITCH_TAX_DAY = 6 * SECONDS * MINUTES


def classify_by_phone_number(records):
    clients_bill = []
    for dic in records:
        result = apply_price_on_bills(dic, clients_bill)
        if type(result) == dict:
            clients_bill.append(result)
    
    return sorted(clients_bill, key=itemgetter('total'), reverse=True)


def apply_price_on_bills(dic, arr):
    # Converting the timestamp to human-readable date (format: HH MM SS)
    end = datetime.fromtimestamp(dic['end'], tz=pytz.timezone('Brazil/East')).strftime('%H %M %S')
    start = datetime.fromtimestamp(dic['start'], tz=pytz.timezone('Brazil/East')).strftime('%H %M %S')

    # Converting the human-readable date to seconds relative to the day
    call_day_seconds_start = (
        (int(start[0:2])*MINUTES*SECONDS)
        + (int(start[6:]))
        + (int(start[3:5])*SECONDS))

    call_day_seconds_end = (
        (int(end[0:2])*MINUTES*SECONDS)
        + (int(end[6:]))
        + (int(end[3:5])*SECONDS))

    price = calculate_prices(dic, call_day_seconds_end, call_day_seconds_start)

    for i in range(len(arr)):
        if dic['source'] == arr[i]['source']:
            return add_to_a_existing_dict(dic, price, i, arr)
    return create_new_dict(dic, price)


def add_to_a_existing_dict(dic, price, i, arr):
    arr[i]['total'] = round(arr[i]['total'] + price, 2)

    return


def create_new_dict(dic, price):
    dic_total = {'source': dic['source'], 'total': round(price, 2)}

    return dic_total


def calculate_prices(dic, end, start):
    if start >= SWITCH_TAX_DAY and start < SWITCH_TAX_NIGHT:
        price_to_pay = 0.36 + (min(abs(end-start), abs(SWITCH_TAX_NIGHT-start))//60)*0.09

    elif start > SWITCH_TAX_NIGHT or start < SWITCH_TAX_DAY:
        free_time = min(abs(end-start), abs(SWITCH_TAX_DAY-start))
        price_to_pay = 0.36 + (((end - start)-free_time)//60)*0.09

    return price_to_pay
