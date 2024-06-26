import aiogram
import logging

from AiogramStorages.storages import PGStorage
from library.openai           import SupportAI

import library.config as env
import library.database as db

is_engine_loaded = True

bot = aiogram.Bot(
    token      = env.BOT_TOKEN, 
    parse_mode = aiogram.types.ParseMode.HTML
)

# POSTGRES LIB
database = db.Database(
    username = env.DB_USERNAME,
    password = env.DB_PASSWORD, 
    host     = env.DB_HOST, 
    port     = env.DB_PORT,
    db_name  = env.DB_NAME,    
)

storage = PGStorage(
    username = env.DB_USERNAME,
    password = env.DB_PASSWORD, 
    host     = env.DB_HOST, 
    port     = env.DB_PORT,
    db_name  = env.DB_NAME,
)

dp     = aiogram.Dispatcher(bot, storage=storage)
engine = None

try:
    engine = SupportAI(env.OPENAI_KEY, 'openai/knowledge').engine
except:
    is_engine_loaded = False
    
    logging.error('OpenAI не был подгружен!')