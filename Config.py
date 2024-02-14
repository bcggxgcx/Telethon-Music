import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14263311"))
    API_HASH = os.environ.get("API_HASH", "c66911c3000c82abc7f41566520ae42c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6754424592:AAEohM33De5b717SXx5Zo_mp7ygAXStVdCE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu2XduyGwv04X3BJmLN-9ZpL6mA6mn_PBGerhXLHwm7fkM8ZhiV_bwTQEEUhe4x56IDM7jwlp2CcpJWbcrER48g2YiWKMtu6Fe3C85rDLsNPfIMmoZix4a774tCz0PHg3ikxjgMcv6fH_PkN9Zysu0oEi8RugnxsJzQwSnh3CTNDtAYApWbQAkdpGw0MkkckbWr_4hMF8dJs4Iu_aMj6fYgi8vtrdJj_uCe1mjRNR2urT43l2qIvU6D_Iy2M3QAmhew1AeXkN6mad3UHAwYVLRmcqG4YzybJOJRY3fMfH-btzVfzQ0kElOc0jiFiu0e4ztDaO26DMamMTvYVlzemDgyA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musicbot_beeebot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5466376297")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
