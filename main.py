from aiogram import Bot, Dispatcher, executor, types
import os
import requests
from keep_alive import keep_alive
keep_alive()
bot           = Bot(token=os.environ.get('token'))
textcaption   = os.environ.get('caption')
image_url     = os.environ.get('image_url')
url_register  = os.environ.get('url_register')
url_login     = os.environ.get('url_login')
domain        = os.environ.get('domain')

dp = Dispatcher(bot)

def get_ip():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        return response.json().get('ip')
    else:
        return "Error fetching IP"
    
@dp.message_handler(commands=['start', 'register'])
async def welcome(message: types.Message):
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = (first_name+last_name).strip()
    password = message.from_user.id
    data_register = {
        "username": full_name,
        "password": password,
        "domain": domain,
        "phone": '',
        "currencyId": '3',
    }
    data_login = {
        "username": full_name,
        "password": password,
        "domain": domain,
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
            await message.reply("អ្នកបង្កើត អាខោន ជោគជ័យ!")
            await message.reply(
                f"Your account: `{full_name}`\n"
                f"Your password: `{password}`\n"
                f"Login: [Link](https://cc24.live?token={token})",
                parse_mode="Markdown"
            )
            await message.answer_photo(photo=image_url, caption=textcaption)

    elif response_data.get('error') == "Duplicate username!":
        response_login = requests.post(
            url_login,
            data=data_login,
        )
        return_login = response_login.json()
        if return_login.get('error') == "Invalid username or password!":
            await message.reply("ឈ្មោះរបស់អ្នកមានរួចហេីយសូមធ្វេីការដូរឈ្មោះតេឡេក្រាមលោកអ្នក")
        elif return_login.get('status') == 200:
            await message.reply(
                f"Your account: `{full_name}`\n"
                f"Your password: `{password}`\n"
                f"Login: [Link](https://cc24.live?token={token})",
                parse_mode="Markdown"
            )
            await message.answer_photo(photo=image_url, caption=textcaption)


@dp.message_handler(commands=['contact'])
async def logo(message: types.Message):
    await message.answer_photo(photo=image_url, caption=textcaption)

if __name__ == '__main__':
    executor.start_polling(dp)
