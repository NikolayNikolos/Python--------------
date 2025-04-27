from address import Address
from mailing import Mailing

to_address = Address("100123", "Москва", "Абрикосова", "1", "5")
from_address = Address("100321", "Архангельск","Виноградная","3","6")

mailing = Mailing(to_address, from_address, "2500", "TRK642")
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.home} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")