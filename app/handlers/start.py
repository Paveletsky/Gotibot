from app.bot                import (dp, bot)
from library.translations   import (l)
from app.boards.common      import (Application)  
from aiogram                import (dispatcher, types)


async def HOOK_START(message: types.Message):
    await message.answer(f"""👋🏻 Hello, {message.from_user.full_name}! 
                                \n\nYou are welcomed by the Goti cryptocurrency exchange support bot 🤖 
                                \n\n🌍 To get started, please select your language 👇.""", 
                         reply_markup=Application().language_menu()
                         )
dp.register_message_handler(HOOK_START, commands=['start'], state='*')