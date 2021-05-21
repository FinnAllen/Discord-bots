import datetime
import discord
from random import randrange

token = 'ODQ1MjAwMzIyNzc5ODA3Nzk0.YKdgJA.5hYY7rsQOeH8r_1VFBgSjFTUc8A'  # token 

client = discord.Client()  # starts the discord client

schedule = {0 : 'Monday: *No raid today.*',
            1 : 'Tuseday: *No raid today.*',
            2 : 'Wednesday: **Encouraged 8-11 EST**',
            3 : 'Thursday: **8-11 EST**',
            4 : 'Friday: **8-11 EST**',
            5 : 'Saturday: **Encouraged 8-11 EST**',
            6 : 'Sunday: *No raid today.*'}
            
flirts = {0 : 'You must be a conjurer because you just cast stoneskin in my pants.',
          1 : 'I hope youre a paladin because I want you to Flash me',
          2 : 'Hey babe, what is the drop rate on those pants?',
          3 : 'Hey babe, I could have sworn I queued for Duty Finder not Cutie Finder.',
          4 : 'Hey is that a linkpearl in your back pocket cause that booty is calling me.',
          5 : 'Dang, even mortal gaze could not turn me away from you.',
          6 : 'Are you a white mage? Because you are sure doing a great job at keeping me up!',
          7 : "I took one look at you and you Y'shtola my heart.",
          8 : "Have you been leveling fisherman? Because I'm hooked!",
          9 : "I gottaa say I'm a real succor for you, you really do make my aetherflow"
          }

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
    elif '?flirt?' in message.content.lower():
      awai message.channel.send(flirts[randrange(10)])
    
            
token = "ODQ1MjAwMzIyNzc5ODA3Nzk0.YKdgJA.X1HmpEjLhse2B0xViNAo5IzNDi0"
client.run(token)  # run the token
