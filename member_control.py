# Standard and discord libraries imports
import os
import threading

import discord
from discord.utils import get

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
        role = get(member.guild.roles, name="rol basico")
        await member.add_roles(role)

    # Whenever an user tries to change role, neglect it if he hasn't enough permisions
    async def on_member_update(self, before, after):
        # First of all, get the new role/s user tries to achieve
        old_roles = set()          # Set for user's old roles
        new_roles = set()          # Set for user's new roles
        
        # This region could be multi-threaded
        '''
            In: Conjunto A, Conjunto B
            Out: Conjunto C (Intersección negada de A y B)
            Politica: FIFO, asignación estática

            Comienza método:
                Res_1 = Set()
                Res_2 = Set()
                Hilo maestro crea 2 hilos

                Hilo_A(procesa_roles(), Conjunto A, Conjunto Res_1)
                Hilo_B(procesa_roles(), Conjunto B, Conjunto Res_2)
                
                Mientras Hilo_A trabajando o Hilo_B trabajando haz
                    Espera a que termine el hilo
                Sincroniza ambos con el hilo maestro
                
                Conjunto C = no (Conjunto Res_1 ^ Conjunto Res_2)

            Fin método
        '''
        first_thread = threading.Thread(target=procesa_roles, args=(before.guild.roles, old_roles))
        second_thread = threading.Thread(target=procesa_roles, args=(after.guild.roles, new_roles))

        first_thread.start() 
        second_thread.start()

        # TODO

        dif_set = new_roles.difference(old_roles)  
        # End of region  
        
        for role in before.guild.roles:
            if role.name == 'Administrator':
                print(f'User: {after.name} has updated his roles to:\n')
                for role in dif_set:
                    print(f'\n - {role.name}')
                return                           # Stop searching, user is admin
        
        # If function continues, we assume user changed roles and hasn't got permisions
        role = get(after.guild.roles, name="Administrator")
        await after.remove_roles(role, f'{after.name} no tienes permiso para realizar esta accion')

# Private threading method
def procesa_roles(conjunto, res):
    for rol in conjunto:
        res.add(rol)
