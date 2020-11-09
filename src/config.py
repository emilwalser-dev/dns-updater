if __name__ == "__main__":
    raise RuntimeError("This file should not be run from the command line.")

import os
from dotenv import load_dotenv


def config():
    load_dotenv()


def required(value):
    if value == None:
        raise ValueError("Some value is not present but is required.")

    return value


GODADDY_KEY = str(required(os.getenv("GODADDY_KEY")))
GODADDY_SECRET = str(required(os.getenv("GODADDY_SECRET")))
GODADDY_DOMAIN = str(required(os.getenv("GODADDY_DOMAIN")))
UPDATE_INTERVAL = int(required(os.getenv("UPDATE_INTERVAL")))
