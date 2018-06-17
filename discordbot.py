import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot (command_prefix = "!")


@client.event
async def on_ready():
    print('Bot\'s ready and has connected to Discord.')

@client.event
async def on_message(message):
    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        # Fetches the user's ID.
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!AMIADMIN'):
        if "457588867801939991" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, 'You\'re an admin!')
        else:
            await client.send_message(message.channel, 'You\'re not an admin, sorry.')
    if message.content.upper().startswith('!SETROLE'):
        userID = message.author.id
        if "457588867801939991" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            if len(args) == 3:
                targetID = args[1]
                role = discord.utils.get(targetID.server.roles, name="Admin")
                await client.add_roles(targetID, role)
                await client.send_message(message.channel, 'Success!')
            else:
                await client.send_message(message.channel, "Insufficent amount of arguments supplied.")
        else:
            await client.send_message(message.channel, 'I\'m sorry, but you need to have the \'ADMIN\' role to use this command.')
            print('Logged: User with ID ' + userID + ' have tried to use the command: \'!setrole\' but failed: Insufficent permissions.')
            
        
    



client.run("NDU3NTc4MTUyMTcyOTc4MTg4.DgbKBg.1ChMLG_AXjTNEAdXI-qVKzN_TwA")

