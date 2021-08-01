# Standard and discord libraries imports
import os
import discord
from dotenv import load_dotenv

# Retrieve Discord's bot verification token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
GUILD_NAME = os.getenv('DISCORD_GUILD_NAME')
GENERAL_CHANNEL = os.getenv('GENERAL_CHANNEL')

# Activate intents on this bot
intents = discord.Intents.default() # Gets the default intents from discord.
intents.members = True # enables members intents on the bot.
# Instatiate a new client
client = discord.Client(intents=intents)

# Verbose client's creation and its intents
print('Client created succesfuly and intents activated')

# Define behaviour for first-time connection with the API
@client.event
async def on_ready():

    # Get server members list
    guild = discord.utils.get(client.guilds, name=GUILD_NAME)
    list_of_members = []                                        # Start an empty list of members
    for member in guild.members:
        list_of_members.append(member.name)

    # Verbose bot and server's info
    print(
        f'{client.user} has established a connection succesfuly!\n'
        f'{guild.name} server connected has id: {guild.id}\n'
        f'Current memebers on guild: {list_of_members}'
    )

    # Check if the bot is part of the server members
    bot_inside = False
    if client.user in guild.members:
        bot_inside = True
    
    print("Is the bot a member? ->", bot_inside)

# Define behaviour for welcoming new users
@client.event
async def on_member_join(member):
    channel = client.get_channel(GENERAL_CHANNEL)
    await channel.send(f'Bienvenido al servidor, {member.name}!')
    await channel.send(file=discord.File('/Users/cjm470/Pictures/LeafyPaleGallinule-size_restricted.gif'))

# Define behaviour for when an user summons the prefix
@client.event
async def on_message(message):

    # First, ignore the prefix if it's written by the bot
    if message.author == client.user:
        return
    
    # If it isn't the bot who send it, then handle it
    # TODO Complete it with a more refined behaviour
    if message.content == ".help":
        response = "Ahora mismo la aplicación esta en desarrollo"
        await message.channel.send(response)

client.run(TOKEN)
