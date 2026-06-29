# config.py
from dotenv import load_dotenv
import os

load_dotenv()

mongouri = os.getenv("DB_URL")
