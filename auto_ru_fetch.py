from fetch_from_autoru import *
from save_offers_to_csv import *

offers = fetch_from_autoru(mark="YAMAHA")
offers.sort(key=lambda x: x.year, reverse=True)
save_offers_to_csv(offers, "auto_ru_yamaha.csv")
