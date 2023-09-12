from aiogram        import (executor, types)
from app.bot        import (dp, storage, database)

from app.handlers   import __all__

import logging

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start bot"),
        types.BotCommand("profile", "Your profile"),
    ])

if __name__ == '__main__':
    logging.basicConfig(format="%(process)d %(levelname)s: %(message)s", level=logging.INFO)    
    executor.start_polling(dp, on_startup=set_default_commands)