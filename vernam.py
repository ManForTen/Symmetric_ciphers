from random import randint

key = ''
keys = ''
final = ''
message = input("Напишите текст, который хотите зашифровать шифром Вернама: ")
message = message.upper()

for symbol in message:
    key = randint(0, 32)
    keys += str(key) + "/"
    final += chr((ord(symbol) + key - 17) % 33 + ord('А'))
print('Зашифрованное сообщение: ', final)
print('Ключ шифрования: ', keys)

final = input('Введите зашифрованное сообщение: ')
keys = input('Введите ключ шифрования: ')

keys = keys.split('/')
message = ''

for i, symbol in enumerate(final):
    if keys[i] != '':
        message += chr((ord(symbol) - int(keys[i]) - 17) % 33 + ord('А'))
print('Расшифрованное сообщение (в нижнем регистре): ', message.lower())