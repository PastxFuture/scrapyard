import json
import os
from datetime import datetime

import discord
import requests

# creating an instance of discord.Client() and assigning it to client
client = discord.Client()

sad_words = ['depressed', 'unhappy', 'sad', 'lonely', 'axiety', 'anxious', 'miserable', 'angry']

encouragement = 'GANBARE!!'

def get_quote():
    # request data from the api URL and store it in response
    response = requests.get('https://zenquotes.io/api/random')
    # convert to json
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote
  
@client.event
async def on_ready():
    print(f'We have logged in as {client}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # The any() function returns True if any item in an iterable are true, otherwise it returns False.
    # Check if any element in list satisfies a condition
    if any(word in msg for word in sad_words):
        await message.channel.send(encouragement)

client.run('ODk1NTk0MDAyODE1MDA4NzY5.YV606Q.My3_AjRxsfd_7b4vFZ-19hTUl2o')
