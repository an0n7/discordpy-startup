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
    
    
class Players {
  List<String> teamNameList = [
    'A team',
    'B team', 
    'C team',
    'D team',  
  ];
  List<String> players;
  Players(this.players);
 
  Map<String, List<String>> getRondomTeam(int teamNum) {
    int fill = players.length % teamNum;
    Map<String, List<String>> teams = {};
    teamNameList.shuffle();
    teamNameList.add('😇 sub');
    players.shuffle();
    int m = players.length ~/ teamNum;
    teamNameList.take(teamNum).toList().asMap().forEach(
        (i, teamName) => teams[teamName] = players.sublist(i * m, i * m + m));
    teams['😇 sub'] = players.sublist(players.length - fill, players.length);
    return teams;
  }
}  
      
    
bot.run(token)
