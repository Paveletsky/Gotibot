import logging

logging.basicConfig(
    format="%(process)d %(levelname)s: %(message)s", 
    level=logging.INFO
)

from aiogram        import (executor, types)
from app.bot        import (dp, storage, database)
from app.handlers   import __all__

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start bot"),
        types.BotCommand("profile", "Your profile"),
    ])

executor.start_polling(dp, on_startup=set_default_commands)