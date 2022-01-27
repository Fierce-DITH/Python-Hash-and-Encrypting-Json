import json
import hashlib

with open ('contentCard.json', 'r') as json_file: #чтение файла JSON
    a = json.load(json_file) 

    for card in a ['card']: # Цикл что бы захватить объекты прохотя по 'card'
        f = hashlib.sha224(card['Creditcard'].encode()) # Шифрование номеров карт в sha224
        r = card['Name'], f.hexdigest(), hash(card['Password']) # Элемент который хранит все объекты + хэширование пароля
        print(json.dumps(r,indent= 1)) # Вывод Json файла в консоль по объектам переменной 'r'
