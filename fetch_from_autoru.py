import requests
import uuid
from Offer import *


def fetch_from_autoru(mark):
    offers = []
    page = 0
    max_page = 100500
    while page <= max_page:
        bodyJson = {
            "catalog_filter": [{"mark": mark}],
            "moto_category": "MOTORCYCLE",
            "section": "used",
            "category": "moto",
            "output_type": "list",
            "page": page,
            "page_size": "100",
        }
        token = uuid.uuid4().hex
        headers = {
            "Content-Type": "application/json",
            "x-csrf-token": token,
            "Cookie": "_csrf_token=%s;" % token,
        }

        response = requests.post(
            "https://auto.ru/-/ajax/desktop/listing/", json=bodyJson, headers=headers
        )

        response_json = response.json()

        # {'total_page_count': 21, 'total_offers_count': 2067, 'page': 2, 'page_size': 100, 'from': 101, 'to': 200, 'current': 2}

        offersJson = response_json["offers"]
        for offerJson in offersJson:
            offer = Offer(
                id=offerJson["saleId"],
                model=offerJson["vehicle_info"]["model_info"]["code"],
                mark=offerJson["vehicle_info"]["mark_info"]["code"],
                price=offerJson["price_info"]["USD"],
                year=offerJson["documents"]["year"],
            )
            offers.append(offer)

        pagination = response_json["pagination"]

        page = page + 1
        max_page = pagination["total_page_count"]

    return offers
