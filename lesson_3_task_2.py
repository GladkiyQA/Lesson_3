from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24", "+79991111111"),
    Smartphone("Apple", "iPhone 15", "+79992222222"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79993333333"),
    Smartphone("Google", "Pixel 6", "+79994444444"),
    Smartphone("OnePlus", "8T", "+79995555555")
]

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.subscriber_number}")