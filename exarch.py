import datetime
import discord

client = discord.Client()  # starts the discord client

schedule = {0 : 'Monday: *No raid today.*',
            1 : 'Tuseday: *No raid today.*',
            2 : 'Wednesday: **Encouraged 8-11 EST**',
            3 : 'Thursday: **8-11 EST**',
            4 : 'Friday: **8-11 EST**',
            5 : 'Saturday: **Encouraged 8-11 EST**',
            6 : 'Sunday: *No raid today.*'}

@client.event
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # login sucessful


@client.event
async def on_message(message):  # event that happens on message
  if message.author != 'Wind-up Exarch':
    # prints message and attributes
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if '?today?' in message.content.lower():
      await message.channel.send(schedule[datetime.datetime.today().weekday()]) # notify user if raid is today
    elif '?schedule?' in message.content.lower():
      await message.channel.send(schedule[0]) 
      await message.channel.send(schedule[1])
      await message.channel.send(schedule[2])
      await message.channel.send(schedule[3])
      await message.channel.send(schedule[4])
      await message.channel.send(schedule[5])
      await message.channel.send(schedule[6])
    elif '?help?' in message.content.lower():
      await message.channel.send('Current Commands:') 
      await message.channel.send('?schedule?') 
      await message.channel.send('?today?') 
    
            

client.run(token)  # run the token
