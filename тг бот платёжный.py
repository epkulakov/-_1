import datetime
import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types, BaseMiddleware
from aiogram.types import LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command

PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7861253104:AAFZ__cAeMZ5UF3-TIY36ScSbJYaLxYpJVA")
dp = Dispatcher()

user_activity = {}

class UserActivityMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data: dict):
        user_id = event.from_user.id
        user_activity[user_id] = datetime.datetime.now()
        return await handler(event, data)

async def check_activity(message: types.Message):
    user_id = message.from_user.id
    last_active = user_activity.get(user_id)

    if last_active:
        last_active_str = last_active.strftime("%H:%M %d.%m.%Y")
        await message.reply(f"Ваша последняя активность была: {last_active_str}")
    else:
        await message.reply("Нет данных об активности")


PRODUCTS = [
]
tovar = ["Яблоки","Сок добрый","Cыр Ирбитски","Конфеты","Молоко"]
opis = ["Яблоки свежие из садов Краснодара","Сок из зелёных яблок","Cыр с жирностью 50%","Конфеты шоколадные, с клубничной начинкой","Молоко с жирностью 1,2%"]
many = [110, 135, 140, 60, 90]
for i in range(5):
    dobavlen = {
  "title": tovar[i],
  "description": opis[i],
  "price": many[i]
}
    PRODUCTS.append(dobavlen)


dp.message.middleware(UserActivityMiddleware())
dp.message.register(check_activity, Command("check_activity"))
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("""
        Привет!
        Через меня ты можешь заказать продукты из магазина "Вкусные продукты".
        Тебе всеволишь нужно выбрать нужный продукт и оплатить его.
        """)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[])

    for idx, product in enumerate(PRODUCTS):
        button = types.InlineKeyboardButton(
            text=product["title"],
            callback_data=f"buy_{idx}"
        )
        keyboard.inline_keyboard.append([button])

    await message.answer("Выберите товар для покупки:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data and c.data.startswith("buy_"))
async def process_buy(callback_query: types.CallbackQuery):
    """Обработка нажатия на кнопку покупки"""
    index = int(callback_query.data.split("_")[1])
    product = PRODUCTS[index]

    prices = [LabeledPrice(label=product["title"], amount=product["price"] * 100)]

    await bot.send_invoice(
        chat_id=callback_query.from_user.id,
        title=product["title"],
        description=product["description"],
        payload=f"product_{index}",
        provider_token=PROVIDER_TOKEN,
        currency="RUB",
        prices=prices,
        start_parameter="test-payment",
    )
    await callback_query.answer()


@dp.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(lambda message: message.successful_payment)
async def successful_payment(message: types.Message):
    await message.answer(
        f"Оплата прошла успешно! Спасибо за покупку")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f"Ошибка: {e}")
#Я не мог толком проверить роботоспособность бота, потомучто не мог подключить оплату(у меня нет ИНН, мне меньше 18)