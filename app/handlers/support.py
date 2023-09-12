import logging

from app.bot                import (dp, bot, database, engine)
from library.translations   import (l)
from app.boards.common      import (Application)  
from aiogram                import (dispatcher, types)
from aiogram.types          import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatActions) 
from asyncio                import (sleep)
from random                 import (randint)


async def BUTTON_q_start(cb: types.CallbackQuery, state: dispatcher.FSMContext):
    try:
        clientLanguage = await database.GetData(
            cb.from_user.id, 'language')
        
        await cb.message.edit_text(text=l('support_welcome', clientLanguage))
        await cb.message.edit_reply_markup(reply_markup=Application(clientLanguage).request_question(1))
    except:
        logging.error(f'User {cb.from_user.id} tried start session, but doesnt exist.')
    ''''''
dp.register_callback_query_handler(BUTTON_q_start, text_contains='OnButton_Help')


async def BUTTON_q_pre(cb: types.CallbackQuery, state: dispatcher.FSMContext):
    try:
        clientLanguage = await database.GetData(
            cb.from_user.id, 'language')

        await cb.message.answer(l('startDialogue', clientLanguage))
        await state.set_state('STATE_typing_question')

        logging.info(f'{cb.from_user.id} started talking session.')
    except:
        logging.error(f'User {cb.from_user.id} tried start session, but doesnt exist.')
    ''''''
dp.register_callback_query_handler(BUTTON_q_pre, text_contains='OnButton_Question_1')


async def HOOK_question(message: types.Message, state: dispatcher.FSMContext):
    try:
        clientLanguage = await database.GetData(
            message.from_user.id, 'language')

        end = KeyboardButton(l('stopSession', clientLanguage))
        board = ReplyKeyboardMarkup(resize_keyboard=True).add(end)

        if message.is_command() or message.text == l('stopSession', clientLanguage):
            await message.reply(
                l('endDialogue', clientLanguage),
                reply_markup=ReplyKeyboardRemove(),
            )

            await state.reset_state()
            logging.info(f'{message.from_user.id} ended talking session.')
        else:
            try:
                data = await state.get_data()
                
                if "is_waiting_answer" in data.keys() and data["is_waiting_answer"]:
                    await message.reply(l('spamMessage'))
                    return
                await state.update_data(is_waiting_answer=True)

                for i in range(randint(11, 19)):
                    await sleep(5)
                    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)

                await message.reply(
                    engine.query(message.text),
                    reply_markup=board
                )

                await state.update_data(is_waiting_answer=False)

            except Exception as e:
                logging.error('Trouble in serverside! OpenAI got error.\n', exc_info=True)
    except:
        logging.error(f'User {message.from_user.id} tried messaging with supporter, but he doesnt exist.', exc_info=True)
    ''''''
dp.register_message_handler(HOOK_question, state='STATE_typing_question')