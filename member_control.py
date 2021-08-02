# Standard and discord libraries imports
import environ_base
import os
import discord

# Define behaviour for administrate guild's users
class MemberListener(environ_base.Environ, discord.Client):
    
    async def on_member_join(self, member):
        channel = self.get_channel(environ_base.Environ.GENERAL_CHANNEL)
        await channel.send(f'Bienvenido al servidor, {member.name}!')

        # Select one defined route depending on current os running on the bot
        file = None
        if (os.path.isfile('/Users/cjm470/Pictures/LeafyPaleGallinule-size_restricted.gif')):
            file = discord.File('/Users/cjm470/Pictures/LeafyPaleGallinule-size_restricted.gif')
        else:
            file = discord.File('c:/Users/Carlos/Documents/Github repos/DiscordBotProject/LeafyPaleGallinule-size_restricted.gif')  
                # Sends hexadecimal value of discord.File file ??

        # If the file still not exists, abort execution
        if file is None:
            return
        
        # Send the file
        await channel.send(file)