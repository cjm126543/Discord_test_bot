import os
from dotenv import load_dotenv

class Environ:

    # Class atributtes
    TOKEN = None
    GUILD_ID = None
    GUILD_NAME = None
    GENERAL_CHANNEL = None

    def __init__(self):
        
        # Retrieve Discord's bot verification token
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD_ID = os.getenv('DISCORD_GUILD_ID')
        self.GUILD_NAME = os.getenv('DISCORD_GUILD_NAME')
        self.GENERAL_CHANNEL = int(os.getenv('GENERAL_CHANNEL'))

        print(f'All enviromental variables loaded successfuly')