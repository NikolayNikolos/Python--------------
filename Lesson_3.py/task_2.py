from smartphone import Smartphone

catalog =  [
    Smartphone("iphone", "15pro", "+7(999)555-55-55"),
    Smartphone("samsung", "S24", "+7(999)111-11-11"),
    Smartphone("google", "8A", "+7(888)222-22-22"),
    Smartphone("POCO", "F3", "+7(777)777-77-77"),
    Smartphone("XIAOMI","13T", "+7(666)666-66-66")
]
for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}."
          f"{smartphone.nomer}")

   