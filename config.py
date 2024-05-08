from pyrogram import filters
import os

class Config:
    API_ID = "27798659"
    API_HASH = "26100c77cee02e5e34b2bbee58440f86"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://jarvisdb:started@kishu.x6a4sr7.mongodb.net/?retryWrites=true&w=majority&appName=Kishu"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["7044783841"])
