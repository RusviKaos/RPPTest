# settings.py
import dotenv
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
#load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASSSWORD = os.getenv("PASSWORD")

pprint(HOST)