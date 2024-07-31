from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    OWNER_ID = int(getenv("OWNER_ID"))
    MONGO_DB_URI = getenv("MONGO_DB_URI")

    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user([OWNER_ID])
