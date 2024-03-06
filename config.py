from pyrogram import filters
import os

class Config:
    API_ID = "24970012"
    API_HASH = "43804289ce8eb7e37a1d680199cd2607"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://jarvisxd45:rajnish68mishra85@atlascluster.xkizs7c.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user(["1983816571"])
