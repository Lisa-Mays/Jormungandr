import discord
from discord import client
from discord import file
#from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import pymysql.cursors
import pymysql

BUF_SIZE = 65536
bot = commands.Bot(command_prefix='!', case_insensitive=True)
currentThread = ""

# When bot connects set the bots activity status message
@bot.event
async def on_ready():
    print('Connected!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Evony"))

# Help Command
@bot.command(pass_context=True)
async def list(ctx):
    if ctx.channel.name in ("avn", "testing", "frisky-mods"):
        await ctx.channel.send("Here is a list of commands: ")
        await ctx.channel.send("List: Displays this help list.")
        await ctx.channel.send("FindID [name]: Lists Monarch ID if known")
        await ctx.channel.send("FindName [ID]: Lists all known names")
        await ctx.channel.send("FindSC [name]: Lists all known Sub Cities")
        await ctx.channel.send("AddName: [name] [monarch id] [alliance]")
        await ctx.channel.send("AddSC: [name] [alliance] [x] [y]")
        await ctx.channel.send("UpdateName: [name] [monarch id] [alliance]")
        await ctx.channel.send("UpdateSC: [name] [alliance] [x] [y]")

# Command to ADD name to database
@bot.command(pass_context=True)
async def AddName(ctx):
    if ctx.channel.name in ("avn", "testing", "frisky-mods"):
        while True:
            monarchname = 'null'
            await ctx.channel.send("Please enter the monarch Name: ")
            def check(m):
                return True
            msg = await bot.wait_for('message', check=check)
            monarchname = msg.content
            await ctx.channel.send("Please enter the Monarch ID:")
            msg = await bot.wait_for('message', check=check)
            monarchid = msg.content
            await ctx.channel.send("Please enter the Alliance:")
            msg = await bot.wait_for('message', check=check)
            alliance = msg.content
            await ctx.channel.send("You entered Monarch Name: "+ monarchname)
            await ctx.channel.send("You entered Monarch ID: "+ monarchid)
            await ctx.channel.send("You entered Alliance: "+ alliance)
            await ctx.channel.send("Is this information correct (y)es (n)o (q)uit?")
            msg = await bot.wait_for('message', check=check)
            response = msg.content
            if response == 'y':
                break
            elif response == 'n':
                continue
            elif response == 'q':
                await ctx.channel.send("Quitting!")
                return
# Connect to evony subcities database hosted on free mysql site
        connection = pymysql.connect(host='hostaddress',
                            port=3306,
                            user='username',
                            password='password',
                            db='dbname',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        sql = "insert into Evony (Name, MonarchID, Alliance) \
               values (%s, %s, %s)"
        cur = connection.cursor()
        cur.execute(sql,(monarchname, monarchid, alliance))
        connection.commit()
        await ctx.channel.send("Data Saved!")

# Command to ADD sub city to database
@bot.command(pass_context=True)
async def AddSC(ctx):
    if ctx.channel.name in ("avn", "testing", "frisky-mods"):
        while True:
            monarchname = 'null'
            await ctx.channel.send("Please enter the monarch Name: ")
            def check(m):
                return True
            msg = await bot.wait_for('message', check=check)
            monarchname = msg.content        
            await ctx.channel.send("Please enter the X Coordinate:")
            msg = await bot.wait_for('message', check=check)
            xcoord = msg.content
            await ctx.channel.send("Please enter the Y Coordinate:")
            msg = await bot.wait_for('message', check=check)
            ycoord = msg.content
            await ctx.channel.send("Please enter the cities culture:")
            msg = await bot.wait_for('message', check=check)
            culture = msg.content
            await ctx.channel.send("Please enter the cities color:")
            msg = await bot.wait_for('message', check=check)
            quality = msg.content

            await ctx.channel.send("You entered Monarch Name: "+ monarchname)
            await ctx.channel.send("You entered X Coordinate: "+ xcoord)
            await ctx.channel.send("You entered Y Coordinate: "+ ycoord)
            await ctx.channel.send("You entered city culture: "+ culture)
            await ctx.channel.send("You entered city color: "+ quality)
            await ctx.channel.send("Is this information correct (y)es (n)o (q)uit?")
            msg = await bot.wait_for('message', check=check)
            response = msg.content
            if response == 'y':
                break
            elif response == 'n':
                continue
            elif response == 'q':
                await ctx.channel.send("Quitting!")
                return   
#Connect to evony subcities database hosted on free mysql site
        connection = pymysql.connect(host='hostaddress',
                            port=3306,
                            user='username',
                            password='password',
                            db='dbname',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        sql = "insert into Evony (Name, X, Y, culture, quality) \
               values (%s, %s, %s, %s, %s)"
        cur = connection.cursor()
        cur.execute(sql,(monarchname, xcoord, ycoord, culture, quality))
        connection.commit()
        await ctx.channel.send("Data Saved!")                    

# Command to FIND sub cities in the database
@bot.command(pass_context=True)
async def AddSC(ctx):
    if ctx.channel.name in ("avn", "testing", "frisky-mods"):
        while True:
            monarchname = 'null'
            await ctx.channel.send("Please enter the monarch Name (partial names allowed): ")
            def check(m):
                return True
            msg = await bot.wait_for('message', check=check)
            monarchname = msg.content        
# Connect to evony subcities database hosted on free mysql site
        connection = pymysql.connect(host='hostaddress',
                            port=3306,
                            user='username',
                            password='password',
                            db='dbname',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        sql = "insert into Evony (Name, X, Y, culture, quality) \
               values (%s, %s, %s, %s, %s)"
        cur = connection.cursor()
        cur.execute(sql,(monarchname, xcoord, ycoord, culture, quality))
        connection.commit()
        await ctx.channel.send("Data Saved!")    

        
        
    
bot.run('BotKey')
