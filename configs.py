

import os


class Config(object):
	API_ID = int(os.environ.get("36956279"))
	API_HASH = os.environ.get("026d4ef35856ac3a8b6c5236b06035fe")
	BOT_TOKEN = os.environ.get("8605781722:AAE85DKqAaLqgAcyyEERJqDC_GHH8XsdAQk")
	UR_CHANNEL = os.environ.get("-1003837896784")
	UR_GROUP = os.environ.get("-1003918351867")
	BOT_USERNAME = os.environ.get("Baddiechut")
	DB_CHANNEL = int(os.environ.get("-1003948528676"))
	BOT_OWNER = int(os.environ.get("Dangerousduck339"))
	DATABASE_URL = os.environ.get("mongodb+srv://Gojoofficial6969@cluster0.tb5l339.mongodb.net")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	HOME_TEXT = os.environ.get("HOME_TEXT")
