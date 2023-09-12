import logging

from app.bot                import (dp, bot, database)
from library.translations   import (l)
from app.boards.common      import (Application)
from aiogram                import (dispatcher, types)
from asyncpg                import (exceptions)
from library.config         import (CODES)


async def HOOK_language(cb: types.CallbackQuery, state: dispatcher.FSMContext):    
    extr_lang = cb.data[2:]
    ''''''
    try:
        if await database.GetUser(cb.from_user.id):
            await database.SetLanguage(cb.from_user.id, extr_lang)
        
        else:
            logging.info(f' Unknown user {cb.from_user.id}. Added.')
            await database.AddUser(cb.from_user.id, extr_lang)

        await cb.message.reply(l('typeAuthcode', extr_lang))
        await state.set_state('STATE_authcode')

    except Exception as err:
        logging.error(err)
    ''''''
dp.register_callback_query_handler(HOOK_language, text_contains='l_')


async def HOOK_auth(message: types.Message, state: dispatcher.FSMContext):
    ''''''
    try:
        clientLanguage = await database.GetData(
            message.from_user.id, 'language')    

        if CODES[message.text]:   
            await message.reply(
                text=f"{l('urBalance', clientLanguage)}", 
                reply_markup=Application(clientLanguage).init_menu()
            )
            
            await database.SetData(
                message.from_user.id, 'authcode', 
                int(message.text)
            )

            logging.info(f'User {message.from_user.id} is registred.')

    except Exception as err:
        logging.error(f'Auth failed: {err}')
        await message.reply(text=f"{l('failedAuth', clientLanguage)}")

    await state.reset_state()
    ''''''
dp.register_message_handler(HOOK_auth, state='STATE_authcode')