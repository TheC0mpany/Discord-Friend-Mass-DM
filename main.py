import discord

client = discord.Client()
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('https://github.com/TheC0mpany/Discord-Friend-Mass-DM')
      print(f"Message sent to: {user.name}")
    except:
       print(f"Message declined for: {user.name}")
       
#Token
client.run('discord token here', bot=False)