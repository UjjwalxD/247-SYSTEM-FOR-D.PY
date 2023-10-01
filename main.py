import discord
import wavelink
from discord.ext import commands
import json
from demon import token
from flask import Flask

app = Flask('app')

class Bot(commands.Bot):

  def __init__(self) -> None:
    intents = discord.Intents.all()

    super().__init__(intents=intents, command_prefix='>')

  async def on_ready(self) -> None:
    print(f'Logged in {self.user} | {self.user.id}')
    activity11 = discord.Activity(type=discord.ActivityType.playing,
                                  name="winkle on fire")
    await bot.change_presence(activity=activity11, status=discord.Status.idle)

  async def setup_hook(self) -> None:
    node: wavelink.Node = wavelink.Node(uri='54.38.198.23:88',
                                        password='stonemusicgay')
    await wavelink.NodePool.connect(client=self, nodes=[node])
    print("Lavalink to chal raha ab")


bot = Bot()
@app.route('/')
def hello_world():
  return 'demon hu bsdk!'
# database
demonop = 'vc.json'
try:
  with open(demonop, 'r') as f:
    voice_channel_data = json.load(f)
except FileNotFoundError:
  voice_channel_data = {}
# end


@bot.event
async def on_ready():
  with open(demonop, 'r') as f:
    voice_channel_data = json.load(f)
  for guild_id, channel_id in voice_channel_data.items():
    channel = bot.get_channel(channel_id)
    if channel is not None:
      vc = await channel.connect(cls=wavelink.Player)
      print(f"reconnected to {guild_id}")

@bot.group(name='247')
async def twentyfourseven(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Please do >247 enable/disable", color=0x2f543)
        await ctx.send(embed=embed)

@twentyfourseven.command()
async def enable(ctx):
    if ctx.author.voice is not None:
        guild_id = ctx.guild.id
        voice_channel_id = ctx.author.voice.channel.id
        voice_channel_data[guild_id] = voice_channel_id

        with open(demonop, 'w') as f:
            json.dump(voice_channel_data, f)

        ujjwalhu = discord.Embed(color=0x2f34e)
        ujjwalhu.set_author(name="Enabled 24/7 For this guild.", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=ujjwalhu)
    else:
        await ctx.send('You need to be in a voice channel to use this command.')

@twentyfourseven.command()
async def disable(ctx):
    guild_id = ctx.guild.id
    if guild_id in voice_channel_data:
        del voice_channel_data[guild_id]
        with open(demonop, 'w') as f:
            json.dump(voice_channel_data, f)
        ujjwalhu = discord.Embed(color=0x2f34e)
        ujjwalhu.set_author(name="Disabled 24/7 for this guild.", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=ujjwalhu)
    else:
        await ctx.send('24/7 is not enabled for this guild.')


app.run(host='0.0.0.0', port=8080)
bot.run(token)



# This code has written in discord.py and wavelink
# Developed by: Ujjwal aka Demon_xD
# Use this code but must provide credits.!
# database used: json
