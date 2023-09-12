import logging

from app.bot                import (dp, bot, database)
from library.translations   import (l)
from app.boards.common      import (Application)
from aiogram                import (dispatcher, types)
from library.config         import (CODES)


async def COMMAND_profile(message: types.Message, state: dispatcher.FSMContext):
    ''''''
    try:
        clientLanguage = await database.GetData(
            message.from_user.id, 'language')
        
        await message.reply(
            text=f"{l('urBalance', clientLanguage)}", 
            reply_markup=Application(clientLanguage).init_menu()
        )

    except:
        await message.answer(f"""👋🏻 Hello, {message.from_user.full_name}! 
                \n\nYou are welcomed by the Goti cryptocurrency exchange support bot 🤖 
                \n\n🌍 To get started, please select your language 👇.""", 
            reply_markup=Application(clientLanguage).language_menu()
        )

    logging.info(f'User {message.from_user.id} executed /profile command.')
    ''''''
dp.register_message_handler(COMMAND_profile, commands=['profile'], state='*')


async def BUTTON_language(cb: types.CallbackQuery, state: dispatcher.FSMContext):    
    ''''''
    try:
        clientLanguage = await database.GetData(
            cb.from_user.id, 'language')

        await cb.message.edit_text(text=l('chooseLang', clientLanguage))
        await cb.message.edit_reply_markup(reply_markup=Application(clientLanguage).language_menu())

    except:
        await cb.message.answer(reply_markup=Application('en').language_menu())
    logging.info(f'User {cb.message.from_user.id} pressed language button.')
    ''''''
dp.register_callback_query_handler(BUTTON_language, text_contains='OnButton_Language')


async def BUTTON_exit(cb: types.CallbackQuery, state: dispatcher.FSMContext):
    ''''''
    try:
        clientLanguage = await database.GetData(
            cb.from_user.id, 'language')

        await cb.message.edit_text( text=f"{l('urBalance', clientLanguage)}" )
        await cb.message.edit_reply_markup( reply_markup=Application(clientLanguage).init_menu() )

    except:
        await cb.message.answer(
            text=l('chooseLang', clientLanguage), 
            reply_markup=Application('en').language_menu()
        )
    ''''''
    logging.info(f'User {cb.message.from_user.id} pressed exit button.')
dp.register_callback_query_handler(BUTTON_exit, text_contains='OnButton_Exit')


async def BUTTON_balance(cb: types.CallbackQuery, state: dispatcher.FSMContext):
    ''''''
    try:
        clientLanguage = await database.GetData(
            cb.from_user.id, 'language')

        authcode = await database.GetData(
            cb.from_user.id, 
            'authcode'
        )

        await cb.message.edit_text(f"{l('cur_balance', clientLanguage)} {CODES[str(authcode)]} \n\n{l('balance', clientLanguage)}")
        await cb.message.edit_reply_markup(reply_markup=Application(clientLanguage).balance_menu())

    except:
        logging.error('User tried check a balance, but he doesnt exist.')
    logging.info(f'User {cb.from_user.id} pressed balance button.')
    ''''''
dp.register_callback_query_handler(BUTTON_balance, text_contains='OnButton_Balance')