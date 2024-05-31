from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, InputFile
from emoji import emojize

import dbFunctions.muslim
from dbFunctions.ullubiy import qr
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btn1 = KeyboardButton('Получить QRCode!')
btn2 = KeyboardButton('Подробнее')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(btn1).add(btn2)
greet_kb_flag = False

k_btn1 = KeyboardButton('Lays')
k_btn2 = KeyboardButton('Pinterest')
k_greet_kb = ReplyKeyboardMarkup()
k_greet_kb.add(k_btn1).add(k_btn2)
k_greet_kb_flag = False


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, emojize("Привет, хочешь немного QR кодов? :winking_face:"),
                           reply_markup=greet_kb)


@dp.message_handler(lambda message: message.text == "Мои баллы")
async def get_description(msg: types.Message):
    dict_of_score = dbFunctions.muslim.get_company(msg.from_user.id)
    buff = 'Ваши баллы: \n'
    print(dict_of_score)
    for i in dict_of_score:
        buff += i + ' ' + str(dict_of_score[i]) + '\n'
    await bot.send_message(msg.from_user.id, buff)


@dp.message_handler(lambda message: message.text == "Получить QRCode!")
async def get_qr_code(msg: types.Message):
    global k_greet_kb_flag
    k_greet_kb_flag = True
    await bot.send_message(msg.from_user.id, "В какой компании вы хотите получить QR код", reply_markup=k_greet_kb)


@dp.message_handler(lambda message: message.text == "Подробнее")
async def get_description(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Возможные команды:\n/score")


@dp.message_handler(lambda message: message.text in ["Pinterest", "Lays"])
async def get_description(msg: types.Message):
    global k_greet_kb_flag

    if k_greet_kb_flag:
        await bot.send_message(msg.from_user.id, "Вот ваш QRCode",
                               reply_markup=ReplyKeyboardMarkup().add(KeyboardButton('Карты')).
                               add(KeyboardButton('Мои баллы')))
        qr_code_photo = InputFile(qr(msg.from_user.id, msg.text.lower()))
        if qr_code_photo:
            await bot.send_photo(chat_id=msg.from_user.id, photo=qr_code_photo)
            k_greet_kb_flag = False
    else:
        await bot.send_message(msg.from_user.id, "Не понимаю")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Не знаю что ты несешь, пиши нормально")


if __name__ == '__main__':
    executor.start_polling(dp)
