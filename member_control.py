# Standard and discord libraries imports
import os
import threading

import discord
from discord.utils import get

# Private threading method
def procesa_roles(roles, conjunto):
    for rol in roles:
        conjunto.add(rol)

# Define behaviour for administrate guild's users
class MemberListener(discord.Client):
    
    # Whenever an user joins, welcome him and give him the basic role
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

        # Assign basic role to new user
        role = get(member.guild.roles, name=environ.BASIC_ROLE_NAME)
        await member.add_roles(role)

    # Whenever an user tries to change role, neglect it if he hasn't enough permisions
    async def on_member_update(self, before, after, environ):
        # First of all, get the new role/s user tries to achieve
        old_roles = set()          # Set for user's old roles
        new_roles = set()          # Set for user's new roles
        
        ### This region is multi-threaded (watch out for possible condition races) ###
        first_thread = threading.Thread(target=procesa_roles, args=(before.guild.roles, old_roles))
        second_thread = threading.Thread(target=procesa_roles, args=(after.guild.roles, new_roles))

        first_thread.start() 
        second_thread.start()

        # Wait for both threads to finish
        first_thread.join()
        second_thread.join()

        dif_set = new_roles.difference(old_roles)  
        ### End of region ###
        
        for role in before.guild.roles:
            if role.name == environ.ADMIN_ROLE_NAME:
                print(f'User: {after.name} has updated his roles to:\n')
                for role in dif_set:
                    print(f'\n - {role.name}')
                return                           # Stop searching, user is admin
        
        # If function continues, we assume user changed roles and hasn't got permisions
        role = get(after.guild.roles, name=environ.ADMIN_ROLE_NAME)
        await after.remove_roles(role, f'{after.name} no tienes permiso para realizar esta accion')