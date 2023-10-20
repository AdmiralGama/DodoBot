import os
import discord
import dotenv
import importlib
import time
import datetime

commands = importlib.import_module('commands', __name__)

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
PREFIX = os.getenv('DISCORD_PREFIX')
COMMANDS = int(os.getenv('COMMANDS_RUN'))

start_time = None

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    activity = discord.Activity(type=discord.ActivityType.watching, name=(PREFIX + 'help'))
    await client.change_presence(activity=activity)
    
    global start_time
    start_time = time.time()

@client.event
async def on_message(message):
    global PREFIX
    global COMMANDS
    global start_time

    if message.author == client.user:
        return
    
    if message.content.startswith(PREFIX):
        COMMANDS += 1

        message_content = message.content[1:].lower()
        args = message_content.split(' ')[1:]
        message_content = message_content.split(' ')[0]

        try:
            response = commands.command_parser(message_content, args)
        except:
            response = 'error'

        if message_content == 'prefix':
            if message.author.id == OWNER_ID:
                PREFIX = args[0]
                dotenv.set_key(dotenv.find_dotenv(), 'DISCORD_PREFIX', PREFIX)
                activity = discord.Activity(type=discord.ActivityType.watching, name=(PREFIX + 'help'))
                await client.change_presence(activity=activity)
                response = 'Prefix changed to ' + PREFIX
            else:
                response = 'ACCESS DENIED'
        if message_content == 'update':
            if message.author.id == OWNER_ID:
                importlib.reload(commands)
                response = 'Updated!'
            else:
                response = 'ACCESS DENIED'
        if message_content == 'stats':
            response = 'Uptime: ' + str(datetime.timedelta(seconds=float(time.time() - start_time))) + '\nTotal Commands Run: ' + str(COMMANDS)

        dotenv.set_key(dotenv.find_dotenv(), 'COMMANDS_RUN', str(COMMANDS))

        if response != '':
            embed = discord.Embed(title=message_content, description=response)
            await message.channel.send(response)
        else:
            COMMANDS -= 1

client.run(TOKEN)