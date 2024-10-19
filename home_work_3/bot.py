import asyncio 
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart()) 
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name} выбери направление курса:", reply_markup=start_keyboard01, )

start_buttons01 = [
    [KeyboardButton(text="GEEKS-направления:"), KeyboardButton(text="GEEKS-контакты:")],
]
start_keyboard01 = ReplyKeyboardMarkup(keyboard=start_buttons01, resize_keyboard=True)

@dp.message(F.text == "GEEKS-направления:") 
async def backend(message: Message):
    await message.answer("Выбери направление:", reply_markup=start_keyboard02)

@dp.message(F.text == "GEEKS-контакты:") 
async def mobile(message: Message):
    await message.answer("""
                ГЛАВНАЯ

            КУРСЫ:

Тестировщик ПО
1С программирование
Менеджер проектов
UX/UI-дизайнер
Fullstack-разработчик
Основы программирования
Mobile-разработчик
Backend-разработчик
Frontend-разработчик
iOS-разработчик
Программирование для детей

            АДРЕСА:
                    
    Бишкек
ул. Ибраимова 103, БЦ “Victory”
    Ош
ул. Мырзалы Аматова 1Б, БЦ Томирис, цокольный этаж (здание Визион)
    Кара-Балта
ул. Кожомбердиева 112, напротив Сах. завода, выше здания Олимпик
    Ташкент
ул. Навбахора 3, 24. Cambridge International University, 3-й этаж. Ориентир: Метро Новза
            
            КОНТАКТЫ:

+996 (557) 05 2018
+996 (507) 05 2018
+996 (777) 05 2018
                         
    ДЛЯ ОБУЧЕНИЯ
office@geeks.kg
                         
    ДЛЯ ПАРТНЕРОВ
marketing@geeks.kg
                         
    Для стажировки
pro@geeks.kg
""", reply_markup=start_keyboard04)


start_buttons02 = [
    [KeyboardButton(text="Backend-разработчик"), KeyboardButton(text="Mobile-разработчик")],
    [KeyboardButton(text="Frontend-разработчик"), KeyboardButton(text="UX/UI-дизайнер")]
]

start_keyboard02 = ReplyKeyboardMarkup(keyboard=start_buttons02, resize_keyboard=True)

start_buttons03 = [
    [KeyboardButton(text="Главное меню"), KeyboardButton(text="Нужна поддержка?")],
]
start_keyboard03 = ReplyKeyboardMarkup(keyboard=start_buttons03, resize_keyboard=True)

start_buttons04 = [
    [KeyboardButton(text="INSTAGRAM"), KeyboardButton(text="WHATSAPP")],
]
start_keyboard04 = ReplyKeyboardMarkup(keyboard=start_buttons04, resize_keyboard=True)


@dp.message(F.text == "Нужна поддержка?") 
async def help(message: Message):
    await message.answer("Чем мы вам можем помочь? Чтобы вернутся в главное меню нажмите '1', Если хотите связаться с админстратором то '2'")


@dp.message(F.text == "Backend-разработчик") 
async def backend(message: Message):
    await message.answer("""
            Кто такой разработчик backend? 
Он ответственен за «внутренние» процессы web-продуктов и выбирает системы для хранения,
гарантирует максимальный уровень производительности при малом объеме сбоев. 
Бэкэнд разработчик продумывает построение логики для реализации разных задумок, 
«строит» фундамент и опорную систему для проекта — от простого сайта для магазина 
одежды до сложных вычислительных систем и нейронных сетей. 
""", reply_markup=start_keyboard03)
    await message.answer_photo("https://geeks.kg/back_media/course/2023/06/21/5c64da3f-db39-463b-815d-75fe8252d468.webp")
@dp.message(F.text == "Mobile-разработчик") 
async def mobile(message: Message):
    await message.answer("""
            Mobile-разработчик:
Никому не секрет, что Android и iOS – это наиболее популярные и распространенные 
мобильные платформы в мире. Следовательно, специальность Mobile-разработчик – это профессия будущего!
Окончив наши курсы по Mobile - разработке, вам останется лишь запустить, опубликовать, 
тестировать, дополнять, своё первое в жизни приложение.
""", reply_markup=start_keyboard03)
    await message.answer_photo("https://geeks.kg/back_media/course/2023/06/21/0673d528-0f95-4466-9b54-e2fc7a0911c8.webp")

@dp.message(F.text == "Frontend-разработчик") 
async def frontend(message: Message):
    await message.answer("""
            Кто такой разработчик backend?
Так называют программистов, которые отвечают за создание внешней стороны (англ. front end) веб-сайтов.
Это клиентская часть сайта, с которой пользователь непосредственно взаимодействует на своем компьютере 
или телефоне, а ещё они организуют логичную работу компонентов сайта: контента, кнопок, внутренних ссылок.
""", reply_markup=start_keyboard03)
    await message.answer_photo("https://geeks.kg/back_media/course/2023/06/21/5a2ea940-aa0c-4271-87c5-533a41c76ec8.webp")
 
@dp.message(F.text == "UX/UI-дизайнер") 
async def uxui(message: Message):
    await message.answer("""
            UX/UI-дизайнер:
Задались вопросом, как стать UX/UI-дизайнером с нуля, тогда вы не зря находитесь на нашем сайте,
здесь вы можете записаться на курсы UX/UI-design, научиться создавать дизайн веб-сайтов и мобильных 
приложений, освоить самый популярный сервис Figma и закреплять обретенные навыки на практике во время обучения.
""", reply_markup=start_keyboard03)
    await message.answer_photo("https://geeks.kg/back_media/course/2023/06/21/a09cf3e2-cc56-4a99-a065-b2bb208fd455.webp")

start_buttons03 = [
    [KeyboardButton(text="Главное меню"), KeyboardButton(text="Нужна поддержка?")],
]
start_keyboard03 = ReplyKeyboardMarkup(keyboard=start_buttons03, resize_keyboard=True)

@dp.message(F.text == "Главное меню") 
async def help1(message: Message):
    await message.answer("Главное меню",reply_markup=start_keyboard01)

@dp.message(F.text == "Нужна поддержка?") 
async def help2(message: Message):
    await message.answer("Чем мы вам можем помочь? Чтобы вернутся в главное меню нажмите '1', Если хотите связаться с админстратором то '2'")

@dp.message(F.text == "1") 
async def help3(message: Message):
    await message.answer("Главное меню", reply_markup=start_keyboard01)

@dp.message(F.text == "2") 
async def help4(message: Message):
    await message.answer("https://t.me/geeks_osh")

@dp.message(F.text == "INSTAGRAM") 
async def insta(message: Message):
    await message.answer("https://www.linkedin.com/company/geekskg/")

@dp.message(F.text == "WHATSAPP") 
async def whats(message: Message):
    await message.answer("https://api.whatsapp.com/send/?phone=996507052018&text&type=phone_number&app_absent=0")

@dp.message()
async def echo(message: Message):
    await message.answer("Чем мы вам можем помочь? Чтобы вернутся в главное меню нажмите '1', Если хотите связаться с админстратором то '2'")


async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
