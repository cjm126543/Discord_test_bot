# Standard and discord libraries imports
import environ_base
import os
import discord

# Define behaviour for administrate guild's users
class MemberListener(discord.Client):
    
    async def on_member_join(self, client, member, environ):
        channel = client.get_channel(environ.GENERAL_CHANNEL)
        await channel.send(f'Bienvenido al servidor, {member.name}!')

        # Select one defined route depending on current os running on the bot
        picture = None
        if (os.path.isfile('/Users/cjm470/Pictures/LeafyPaleGallinule-size_restricted.gif')):
            picture = discord.File('/Users/cjm470/Pictures/LeafyPaleGallinule-size_restricted.gif')
        else:
            picture = discord.File('c:/Users/Carlos/Documents/Github repos/DiscordBotProject/LeafyPaleGallinule-size_restricted.gif')  

        # If the file still not exists, abort execution
        if picture is None:
            return
        
        # Send the file
        await channel.send(file=picture)