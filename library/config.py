from environs import Env
import os

env = Env()
env.read_env()

BOT_TOKEN   = env.str("BOT_TOKEN")
DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST     = env.str("DB_HOST")
DB_PORT     = env.str("DB_PORT")
DB_NAME     = env.str("DB_NAME")

OPENAI_KEY  = env.str("OPENAI_KEY")

# КОДЫ АВТОРИЗАЦИИ - БАЛАНС АККАУНТА
CODES = {
    '83519582': '€19,989.00',
    '26492543': '€19,989.00',
    '73710585': '€19,989.00',
    '51309873': '€19,989.00',

    '877110485': '€27,307.00',
    '118774309': '€27,307.00',
    '302875775': '€27,307.00',
    '619462239': '€27,307.00',

    '461934759': '€38,541.00',
    '261057340': '€38,541.00',
    '47295730': '€38,541.00',
    '274562950': '€38,541.00',
    '80988251': '€38,541.00',
}