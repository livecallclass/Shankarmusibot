from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29687224))
API_HASH = getenv("API_HASH", c543dbfe3007000fbecbd48c10731a55)
BOT_TOKEN = getenv("BOT_TOKEN", 6723628824:AAHdyEH9Pbmz8N9HJA81umH_e1-8o3MmUOo)
OWNER_ID = int(getenv("OWNER_ID", 6427042108))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6427042108").split()))
