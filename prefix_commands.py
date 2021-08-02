# Standard and discord libraries imports
import os
import discord

# Define behaviour for when an user summons the prefix
class PrefixListener(discord.Client):

    async def on_message(self, message):
        print(f'Now listening to prefix petitions...')          # Prints message twice, dkw

        # First, ignore the prefix if it's written by the bot
        if message.author == self.user:
            return
        
        # If it isn't the bot who send it, then handle it
        # TODO Complete it with a more refined behaviour
        if message.content == ".help":
            response = "Ahora mismo la aplicación esta en desarrollo"
            await message.channel.send(response)

        # Other behaviours depending on the command
        if message.content == ".TODO":
            pass