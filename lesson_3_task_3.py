from Adress import Adress
from Mailing import Mailing


to_address = Adress("123456", "Город1", "Улица1", "10", "5")
from_address = Adress("999999", "Город2", "Улица2", "20", "3")
mailing = Mailing(to_address, from_address, 200, "qwix123456")


print(f"Отправление {mailing.track} из {from_address.index}, \
{from_address.city}, {from_address.street}, {from_address.house} - \
{from_address.flat} в {to_address.index}, {to_address.city}, \
{to_address.street}, {to_address.house} - {to_address.flat}. \
Стоимость {mailing.cost} рублей.")
