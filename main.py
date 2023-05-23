from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

# Вставьте свой токен:
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='help',
                   description='Справка по работе бота'),
        BotCommand(command='support',
                   description='Поддержка'),
        BotCommand(command='contacts',
                   description='Другие способы связи'),
        BotCommand(command='payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)