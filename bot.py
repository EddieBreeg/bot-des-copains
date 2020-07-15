import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')

lib={'*mauvais': 'data/mauvais.wav',
    '*cafard': "data/cafard.wav"}

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_message(message):
    start=message.content.split(' ')[0] #premier mot du message
    if start in lib:
        if message.author.voice==None: # utilisateur non connecte en vocal
            await message.channel.send("Connecte toi en vocal stp...")
        elif bot.voice_clients==[]: # bot non connecte
            await message.author.voice.channel.connect() #on se connecte
        elif bot.voice_clients[0].channel!=message.author.voice.channel: # bot connecte MAIS pas au bon endroit
            await bot.voice_clients[0].move_to(message.author.voice.channel) # on bouge
        bot.voice_clients[0].play(discord.FFmpegOpusAudio(lib[start])) #on encode et joue le bon ficher

token=open("token.key").read()
bot.run(token)
