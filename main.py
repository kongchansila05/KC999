import os
import telebot
import requests

API_KEY = os.getenv('API_KEY',
                    '7627695687:AAFMXIBq1O2WqnnKx5V4-JXcflNv8HWjkjk')
IMAGE_URL = "https://i.ibb.co/5sxj6wj/KC-2.jpg"
bot = telebot.TeleBot(API_KEY)

url_register = "https://api.cc24.live/api/cs_player/register"
url_login = "https://api.cc24.live/api/cs_player/login_v2"


def get_ip():
    # Using a free IP API to get the client's public IP
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        return response.json().get('ip')
    else:
        return "Error fetching IP"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    data_register = {
        "username": message.from_user.first_name,
        "password": message.from_user.id,
        "domain": 'kc999.co',
        "phone": '',
        "currencyId": '3',
    }

    data_login = {
        "username": message.from_user.first_name,
        "password": message.from_user.id,
        # "password": '801984912',
        "domain": 'kc999.co',
        "clientIP": get_ip(),
    }

    response_register = requests.post(
        url_register,
        data=data_register,
    )
    response_data = response_register.json()
    if response_data.get('code') == 200:
        response_login_true = requests.post(
            url_login,
            data=data_login,
        )
        login = response_login_true.json()
        if login.get('status') == 200:
            token = login['data']['token']
            bot.send_message(chat_id, f"អ្នកបង្កើត អាខោន ជោគជ័យ!")
            bot.send_message(
                chat_id, f"Your account: `{message.from_user.first_name}`\n"
                f"Your password: `{message.from_user.id}`\n",
                parse_mode="Markdown")
            bot.send_message(chat_id,
                             f"Login: https://cc24.live?token={token}")
            caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻  @KC999_CS  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"
            bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)
        return
    elif response_data.get('error') == "Duplicate username!":
        response_login = requests.post(
            url_login,
            data=data_login,
        )
        return_login = response_login.json()
        if return_login.get('error') == "Invalid username or password!":
            bot.send_message(
                chat_id,
                f"ឈ្មោះរបស់អ្នកមានរួចហេីយសូមធ្វេីការដូរឈ្មោះតេឡេក្រាមលោកអ្នក")
            return
        else:
            if return_login.get('status') == 200:
                bot.send_message(chat_id, f"អ្នកមាន អាខោន រួចហើយ!")
                bot.send_message(
                    chat_id,
                    f"Your account: `{message.from_user.first_name}`\n"
                    f"Your password: `{message.from_user.id}`\n",
                    parse_mode="Markdown")
                token = return_login['data']['token']
                bot.send_message(chat_id,
                                 f"Login: https://cc24.live?token={token}")
                caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻 @KC999_CS  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"
                bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)


@bot.message_handler(commands=['register'])
def send_register(message):
    chat_id = message.chat.id
    data_register = {
        "username": message.from_user.first_name,
        "password": message.from_user.id,
        "domain": 'kc999.co',
        "phone": '',
        "currencyId": '3',
    }

    data_login = {
        "username": message.from_user.first_name,
        "password": message.from_user.id,
        # "password": '801984912',
        "domain": 'kc999.co',
        "clientIP": get_ip(),
    }

    response_register = requests.post(
        url_register,
        data=data_register,
    )
    response_data = response_register.json()
    if response_data.get('code') == 200:
        response_login_true = requests.post(
            url_login,
            data=data_login,
        )
        login = response_login_true.json()
        if login.get('status') == 200:
            token = login['data']['token']
            bot.send_message(chat_id, f"អ្នកបង្កើត អាខោន ជោគជ័យ!")
            bot.send_message(
                chat_id, f"Your account: `{message.from_user.first_name}`\n"
                f"Your password: `{message.from_user.id}`\n",
                parse_mode="Markdown")
            bot.send_message(chat_id,
                             f"Login: https://cc24.live?token={token}")
            caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻  @KC999_CS  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"
            bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)
        return
    elif response_data.get('error') == "Duplicate username!":
        response_login = requests.post(
            url_login,
            data=data_login,
        )
        return_login = response_login.json()
        if return_login.get('error') == "Invalid username or password!":
            bot.send_message(
                chat_id,
                f"ឈ្មោះរបស់អ្នកមានរួចហេីយសូមធ្វេីការដូរឈ្មោះតេឡេក្រាមលោកអ្នក")
            return
        else:
            if return_login.get('status') == 200:
                bot.send_message(chat_id, f"អ្នកមាន អាខោន រួចហើយ!")
                bot.send_message(
                    chat_id,
                    f"Your account: `{message.from_user.first_name}`\n"
                    f"Your password: `{message.from_user.id}`\n",
                    parse_mode="Markdown")
                token = return_login['data']['token']
                bot.send_message(chat_id,
                                 f"Login: https://cc24.live?token={token}")
                caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻 @KC999_CS  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"
                bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)


@bot.message_handler(commands=['contact'])
def send_contact_info(message):
    chat_id = message.chat.id  # Get the chat ID to send the message directly

    # Caption for the photo
    caption = "សំរាប់ចម្ងល់ឬបញ្ហាផ្សេងៗ នឹង ដាក់/ដក ប្រាក់ ចុចទីនេះ 👉🏻 @KC999_CS  បញ្ជាក់៖ នេះជាម៉ាសុីនសម្រាប់តែបង្កើតអាខោន មិនចេះឆ្លើយតបទេ។ សូមអរគុណ!"

    # Send the photo with the caption
    bot.send_photo(chat_id, photo=IMAGE_URL, caption=caption)


bot.polling()
