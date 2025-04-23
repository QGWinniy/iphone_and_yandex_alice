import sys
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

api_id = 11111111111
api_hash = '-------'
bot_username = '@alice_speaker_bot'

if len(sys.argv) < 2:
    print("Не передано сообщение")
    sys.exit(1)

message = sys.argv[1]

client = TelegramClient('session_name', api_id, api_hash)

client.connect()

if not client.is_user_authorized():
    print("Первый запуск. Авторизуемся...")
    phone = input("Введи свой номер телефона (в международном формате, например +79876543210): ")
    client.send_code_request(phone)

    code = input("Введи код из Telegram: ")

    try:
        client.sign_in(phone, code)
    except SessionPasswordNeededError:
        password = input("Телега защищена двухфакторкой. Введи пароль: ")
        client.sign_in(password=password)

print("Отправляю сообщение алисе...")
client.send_message(bot_username, message)
print("✅ Сообщение отправлено.")

client.disconnect()
