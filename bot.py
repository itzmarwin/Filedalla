#(©)Codexbotz

from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT

name =""" (lol) """

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.web_app = None  # Health Check के लिए नया variable

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Health Check Web Server Setup
        self.web_app = web.Application()
        self.web_app.router.add_get("/health", lambda request: web.Response(text="OK"))  # यहाँ नया code
        
        # पुराना web server setup
        app = web.AppRunner(await web_server())
        await app.setup()
        
        # दोनों servers को combine करें
        self.web_app.add_subapp("/", app.app)
        
        # Server start करें
        bind_address = "0.0.0.0"
        await web.TCPSite(self.web_app, bind_address, PORT).start()

        # बाकी initialization code यहाँ...
        # [आपका मूल initialization कोड यहाँ रहेगा]

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
