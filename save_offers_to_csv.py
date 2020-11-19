import os
import csv

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fields = ["id", "mark", "model", "year", "price"]


def save_offers_to_csv(offers, file_name):
    path = os.path.join(__location__, file_name)
    with open(path, mode="w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for offer in offers:
            row = {
                "id": offer.id,
                "mark": offer.mark,
                "model": offer.model,
                "year": offer.year,
                "price": offer.price,
            }
            writer.writerow(row)
