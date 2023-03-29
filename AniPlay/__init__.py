from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "29728392")),
    api_hash= environ.get("API_HASH", "2b3ee4e6b67b568b09b1b6560dba30af"),
    bot_token= environ.get("TOKEN", "5924561801:AAF29EvpFXj6-BNmtL7cTiE9Ud5uDcrwdek")
)
