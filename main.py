import asyncio
import time

from aiogram import Bot, executor, types, Dispatcher
import os
from keyboards import inline_keyboard
from aiogram.dispatcher.filters import Command
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


load_dotenv()
bot = Bot(token=os.getenv("token_id"))
dp = Dispatcher(bot)


@dp.message_handler(Command('start'))
async def main(message: types.Message):
    await message.delete()
    await bot.send_message(
        message.from_user.id,
        "Привет, данный бот поможет тебе отслеживать актуальную информацию, "
        "связанную с поступлением. Выбери одну или несколько команд, которые тебе нужны =)"
        "\n"
        "\nПМ -- уведомит тебя, когда появятся списки о зачислении на ПМ"
        "\nИВТ -- уведомит тебя, когда появятся списки о зачислении на ИВТ"
        "\nОбщежитие -- уведомит тебя, когда появятся списки о заселении в общежитие."
        ""
        "\n\nЕсли у тебя есть какие-то вопросы про учебу в МИСИС'е -- @nikitasss1"
    , reply_markup=inline_keyboard
    )


@dp.callback_query_handler(text="ПМ")
async def PM(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Успешно запущено!",
                         reply_markup=inline_keyboard)
    await pm_search(message=call.message)



@dp.callback_query_handler(text="ИВТ")
async def PM(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Успешно запущено!",
                         reply_markup=inline_keyboard)
    await ivt_search(message=call.message)


@dp.callback_query_handler(text="Общежитие")
async def PM(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Успешно запущено!",
                         reply_markup=inline_keyboard)
    await obsh_search(message=call.message)

async def main1():
    await dp.start_polling()

async def main2():
    while True:
        await asyncio.sleep(1)

async def pm_search(message: types.Message):
    while True:
        url = requests.get("https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-COMM-O-010304")
        # url = requests.get("https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-010304")
        text = BeautifulSoup(url.text, 'lxml')
        done = text.find("tbody")
        if "Зачислен" in done.text:
            await message.answer('Появились списки для зачисления на направление: Прикладная математика')
            break


async def ivt_search(message: types.Message):
    while True:
        url = requests.get("https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-COMM-O-090300")
        text = BeautifulSoup(url.text, 'lxml')
        done = text.find("tbody")
        if "Зачислен" in done.text:
            await message.answer('Появились списки для зачисления на направление: Информатика и вычислительная техника')
            break


async def obsh_search(message: types.Message):
    while True:
        url = requests.get("https://misis.ru/applicants/accommodation/memo/")
        text = BeautifulSoup(url.text, 'lxml')
        done = len(text.find_all("p"))
        if done >= 23:
            await message.answer("Появились списки для заселения")
            break


async def main_task():
    await asyncio.gather(
        main1(),
        main2()
    )
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main_task())