from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")

    
    OWNER_ID = "7044783841"
    MONGO_DB_URI = "mongodb+srv://jarvisdb:started@kishu.x6a4sr7.mongodb.net/?retryWrites=true&w=majority&appName=Kishu"

    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user([7044783841])
