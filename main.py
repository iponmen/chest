import discord
import os
import _thread as thread
import random

import glb
import control
from imports import pieces
from imports import action
from imports import debugging
from imports import general
from imports import game

confirmCmds = []

##        ----------           ##
""" For command line commands """
##        ----------           ##
print("start")
try:
    thread.start_new_thread(control.cmdThead, ())
except:
    print("Error in cmd Thread")



##           ------------------------          ##
""" For listening to discord msg and commands """
##           ------------------------          ##
client = discord.Client()

@client.event
async def on_ready():
    channel1 = client.get_channel(843214787856957460)
    print('We have logged in as {0.user}'.format(client))
    await channel1.send(general.printBoard())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    x = []
    if message.content.startswith('!move'):
        x = str(message.content).split(" ")[1:]
        temp = game.move(general.cord(x[0]), general.cord(x[1]))
        if(temp != False):
            await message.channel.send(general.printBoard())
        else:
            await message.channel.send(general.printBoard())
            await message.channel.send("wrong")
    elif message.content.startswith('!board'):
        await message.channel.send(general.printBoard())
    elif message.content.startswith('!restart'):
        confirmCmds.append(game.start)
        await message.channel.send("send !confirm to really restart the game")
    elif message.content.startswith('!confirm'):
        if len(confirmCmds) > 0 :
            for i in confirmCmds:
                i()
    elif message.content.startswith('!help'):
        await message.channel.send("!help -------------------------\n    !move a0 a0\n    !board\n    !restart")

    elif "f u" in message.content:
        randomd = random.randint(1, 3)
        if(randomd == 1):
            await message.channel.send("heeyyyyyy! rude you")
        else:
            await message.channel.send("TEACHER, he... he.. hhe.. hehehehehehehehehe\n\nteacher: how dare you assume someone's gender, OUT!!\n\nwhy is the programmer of this thing so braindead, probably because of summer\n\n WHAT TIME is IT, SUMMER TIME")
    elif message.content.startswith('!you'):
        whatIam = str(message.content).split(" ")[1]
        await message.channel.send(f"yep, I AMM { whatIam }")
    elif message.content.startswith('!'):
        await message.channel.send("Do !help to see avaliable cmds")

    

    resp = game.tick()
    if resp["id"] != 0:
        await message.channel.send(resp["description"])


client.run("ODMzMDU5NDM2MTkyOTg5MjE0.YHs1Dw.Fedo_afgKC9-lKHrSE8WO4XVZaQ")