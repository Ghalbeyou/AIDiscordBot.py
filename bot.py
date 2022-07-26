import os
import discord
from discord.ext import commands
import requests
bot = commands.Bot(command_prefix='P!')
key = "Your BrainShop.Ai Key"
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # check if the message is asked in the specific channel
    if message.channel.id == your_ai_channel:
    # create a embed for processing
        embed = discord.Embed(title="Working ...",         description="Please wait !", color=0x00ff00)
        embed.set_footer(text="Powered by: ! Arash#9999")
        msgj = await message.channel.send(embed=embed)
        # get users id
        user_id = message.author.id
        try:
            msg = requests.get(f"http://api.brainshop.ai/get?key={key}&uid={user_id}&msg={message.content}")
            msg = msg.json()
            msg = msg['cnt']
            if "Acobot Team" in msg:
                msg = "I was created by Arash"
            if "acobot.ai" in msg:
                # msg.replace("acobot.ai", "Ghalbeyou Discord")
                msg = "I was created by Arash"
            await msgj.edit(embed=None, content=msg)
        except:
            await msgj.edit(embed=None, content="Error!")
        return
    else:
        return
bot.run("Your Bots Token!")
