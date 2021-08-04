import os
from dotenv import load_dotenv

class Environ:

    # Class atributtes
    TOKEN = None
    GUILD_ID = None
    GUILD_NAME = None
    GENERAL_CHANNEL = None
    BASIC_ROLE_ID = None
    BASIC_ROLE_NAME = None
    ADMIN_ROLE_NAME = None

    def __init__(self):
        
        # Retrieve Discord's bot verification token
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD_ID = os.getenv('DISCORD_GUILD_ID')
        self.GUILD_NAME = os.getenv('DISCORD_GUILD_NAME')
        self.GENERAL_CHANNEL = int(os.getenv('GENERAL_CHANNEL'))
        self.BASIC_ROLE_ID = os.getenv('BASIC_ROLE_ID')
        self.BASIC_ROLE_NAME = os.getenv('BASIC_ROLE_NAME')
        self.ADMIN_ROLE_NAME = os.getenv('ADMIN_ROLE_NAME')

        print(f'All enviromental variables loaded successfuly')