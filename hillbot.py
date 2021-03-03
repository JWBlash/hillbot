#!/usr/bin/python3
import os

import discord
from dotenv import load_dotenv

load_dotenv()
HILLBOT_TOKEN = os.getenv('HILLBOT_TOKEN')

hillbot = discord.Client()

@hillbot.event
async def on_ready():
    for guild in hillbot.guilds:
        print(
            f'{hillbot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        await guild.system_channel.send('Online and checking emails.')

@hillbot.event
async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.name == 'Cedar Rapids':
                await member.guild.system_channel.send(f'{member.name} is just chillin\' in Cedar Rapids.')
                print(f'{member.name} is just chillin\' in Cedar Rapids.')

hillbot.run(HILLBOT_TOKEN)

