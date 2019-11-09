from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def neko(ctx):
    await ctx.send('meow')
    
    
var channel = (e.message.author as Member).voiceState.channel;
      List<String> users = channel.connectedUsers
          .map((voiceState) => voiceState.user.username)
          .toList();
    
    
bot.run(token)
