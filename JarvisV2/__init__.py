import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from JarvisV2.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://telegra.ph/file/d4fc1dc38f65962d4be3f.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "Jarvis",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def JarvisV2():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]ᴊᴀʀᴠɪs")
    LOG.print("[bold yellow]ʏᴏᴜʀ ʙᴏᴛ sᴛᴀʀᴛ.............")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(JarvisV2())    
