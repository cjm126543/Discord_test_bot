# Standard and discord libraries imports
import discord

# Custom modular imports
import prefix_commands
import member_control
import environ_base

# Activate intents on this bot
intents = discord.Intents.default() # Gets the default intents from discord.
intents.members = True # enables members intents on the bot.

# Instatiate main classes (Singleton pattern used)
environ_vars = environ_base.Environ()               # Environ data class
base_client = discord.Client(intents=intents)       # Discord's API default client
member_admin = member_control.MemberListener()      # Member administrator listener
listener = prefix_commands.PrefixListener()         # Prefix messaging listener

# Verbose client's creation and its intents
print('Client created succesfuly and intents activated')

# Define behaviour for first-time connection with the API
@base_client.event
async def on_ready():

    # Get server members list
    guild = discord.utils.get(base_client.guilds, name=environ_vars.GUILD_NAME)
    list_of_members = []                                        # Start an empty list of members
    for member in guild.members:
        list_of_members.append(member.name)

    # Verbose bot and server's info
    print(
        f'{base_client.user} has established a connection succesfuly!\n'
        f'{guild.name} server connected has id: {guild.id}\n'
        f'Current memebers on guild: {list_of_members}'
    )

    # Check if the bot is part of the server members
    bot_inside = False
    if base_client.user in guild.members:
        bot_inside = True
    
    print("Is the bot a member? ->", bot_inside)

# Prefix summon behaviour (specified in prefix_commands.py file)
@base_client.event
async def on_message(message):
    print(f'Now listening to prefix petitions...')          # Prints message twice, dkw
    await listener.on_message(message)

# New member joining behaviour (specified in member_control.py file)
@base_client.event
async def on_member_join(member):
    print(f'New member {member.name} has joined the guild')
    await member_admin.on_member_join(base_client, member, environ_vars)

# Run standard client
base_client.run(environ_vars.TOKEN)