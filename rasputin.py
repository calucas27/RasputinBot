import discord
import asyncio
import random
import youtube_dl
from bs4 import BeautifulSoup
import urllib3
import urllib.request
import urllib.parse
import re
import binascii
import time

client = discord.Client()

version = 'Rasputin 1.0 -- Written by: http://www.github.com/calucas27'

clienttime = (time.strftime("%H:%M:%S"))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(clienttime,':Bot started!')
    print('=======')

@client.event
async def on_message(message):
    if message.content.startswith('#hello'):
        await client.send_message(message.channel, 'Hello! My name is Rasputin!')

    if message.content.startswith('#ver'):
        await client.send_message(message.channel, version)

    if message.content.startswith('#help'):
        helpfile = open('commands.txt','r')
        commands = helpfile.read()
        helpfile.close()
        await client.send_message(message.channel,commands)

    if message.content.startswith('#wordsalad'):
        lines = open('dictionary.txt').read()
        line = lines[0:]
        words = line.split()
        myarray = []
        for a in range(10):
            myword = random.choice(words)
            myarray.append(myword)
        await client.send_message(message.channel,myarray)

    if message.content.startswith('#yt'):
        raw = message.content
        title = raw.replace('#yt',"")
        query_string = urllib.parse.urlencode({"search_query" : title})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        video = ("http://www.youtube.com/watch?v=" + search_results[0])
        await client.send_message(message.channel, video)

    if message.content.startswith('#frombinary'):
        raw = message.content
        title = raw.replace('#frombinary',"")
        n = int(title, 2)
        toascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        await client.send_message(message.channel,toascii)

    if message.content.startswith('#tobinary'):
        raw = message.content
        title = raw.replace('#tobinary',"")
        tobinary = bin(int.from_bytes(title.encode(), 'big'))
        await client.send_message(message.channel,tobinary)

client.run('Your client ID goes here!')
