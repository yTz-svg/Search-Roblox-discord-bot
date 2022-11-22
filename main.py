import disnake
import requests
from disnake.ext import commands
import time
import json
from disnake.ext import tasks 
from random import choice 
from disnake.ui import Button

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.slash_command(name='help',description='All commands')
async def help(inter):
    button = Button(label='Invite RoCity',style=disnake.ButtonStyle.green,url='https://discord.com/oauth2/authorize?client_id=1041164166318260295&scope=bot&permissions=8')
    button2 = Button(label='Smartphone',style=disnake.ButtonStyle.green)
    view = disnake.ui.View()
    view.add_item(button)
    view.add_item(button2)
    async def  button_callback(interaction):
            embed = disnake.Embed(title='Smarthphone Support',color=disnake.Colour.green())
            embed.set_image(url='https://cdn.discordapp.com/attachments/1013475156464783451/1042551406453858416/image.png')
            await interaction.response.send_message(embed = embed,ephemeral=True)

    button2.callback = button_callback
    embed = disnake.Embed(title='RoCity commands', description='Here are all the commands for RoCity' , color=disnake.Colour.green())
    embed.add_field(name="Search Roblox", value="Subcommands: `username_name` `asset_id` `limited_id` `limited_similar` `gamepass_id ` `clothe_id [CopyRight Verify/Donwload]` `roblox_status` \n Lookup information directly from the roblox API", inline=False)
    embed.add_field(name="Cookie Edit Roblox", value="Subcommands: `cookie_checker`\n Lookup information from a cookie and edit it", inline=False)
    embed.add_field(name="Cassino", value="Subcommands: `development [yTz] [strawhats]`", inline=False)
    embed.add_field(name="Bot Support", value="Subcommands: `support` `status` `credits` `help`\n Bot information and we are in beta ", inline=False)
    embed.add_field(name="Premium", value="Subcommands: `Trade_Ads` `Auto_accept` \n 3$ BTC/ETH ", inline=False)
    embed.set_footer(text='Version: Beta')
    await inter.response.send_message(embed = embed, view=view)

@bot.slash_command(name='credits',description='Rocity Credits')
async def user(inter):
        button = Button(label='Developer',style=disnake.ButtonStyle.green)
        button2 = Button(label='Api contribuitor',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        view.add_item(button2)

        async def  button_callback(interaction):
            embed = disnake.Embed(title='yTz#1000',description='14y / Brazil \nWeb Developer \nIntermediary Python', color=disnake.Colour.green())
            embed.set_image(url='https://cdn.discordapp.com/avatars/776854360280924210/a_5aaa869ca9af4110046c5dc08e509f1f.gif?size=1024')
            await interaction.response.send_message(embed = embed,ephemeral=True)
        async def  button_callback2(interaction):
            embed = disnake.Embed(title='Rolimon#0865',description='I used to trade on Roblox, but now I only have time to work on Rolimons \nOwner/developer of the Roblox trading site https://www.rolimons.com/', color=disnake.Colour.green())
            embed.set_image(url='https://cdn.discordapp.com/attachments/1013475156464783451/1042191355524435988/unknown.png')
            await interaction.response.send_message(embed = embed,ephemeral=True)
    
        button.callback = button_callback
        button2.callback = button_callback2
        embed = disnake.Embed(title="Credits",description="Thanks to everyone who is using our bot", color=disnake.Colour.green())
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1013475156464783451/1041780690171220039/unknown.png')
        embed.add_field(name="Developer", value="yTz#1000", inline=True)
        embed.add_field(name="Api contributor", value="Rolimon#0865", inline=True)
        embed.add_field(name='contributor', value=inter.author, inline=False)
        embed.add_field(name='Trade', value="https://www.rolimons.com/ \n https://rblx.trade/", inline=False)
        await inter.response.send_message(embed = embed,ephemeral=False, view=view)
    
@bot.slash_command(name='status',description='Rocity/Discord status')
async def user(inter):
    try:
        button = Button(label='Deails',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        async def  button_callback(interaction):
            embed.set_image(url='https://cdn.discordapp.com/attachments/1013475156464783451/1042199147517857903/unknown.png')
            await interaction.response.send_message(embed = embed,ephemeral=True)

        button.callback = button_callback
        embed = disnake.Embed(title=f"RoCity Status",description="", color=disnake.Colour.green())
        discord = requests.get('https://discordstatus.com/api/v2/incidents.json').json()
        embed.add_field(name="Status", value="✅", inline=True)
        embed.add_field(name="Client", value=discord['page']['id'], inline=True)
        embed.add_field(name="Server", value=discord['page']['time_zone'], inline=False)
        embed.add_field(name="Update", value=discord['page']['updated_at'], inline=False)
        await inter.response.send_message(embed = embed,ephemeral=False,view=view)
    except:
        embed = disnake.Embed(title=f"Discord Api Death",description="Loading...", color=disnake.Colour.red())
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='asset_id', description="Search for intems places gears...")
async def user(inter,intem_id:int):
    try:
        button = Button(label='Source',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        async def  button_callback(interaction):
            embed = disnake.Embed(title='Json',description=f'```{read}```', color=disnake.Colour.dark_theme())
            await interaction.response.send_message(embed = embed,ephemeral=True)

        button.callback = button_callback
        request = requests.get(f"https://api.roblox.com/Marketplace/ProductInfo?assetId={intem_id}")
        read = request.json()
        embed = disnake.Embed(title=read['Name'],description=read['Description'], color=disnake.Colour.green())
        embed.add_field(name="TargetId", value=read['TargetId'], inline=True)
        embed.add_field(name="Creator", value=read['Creator']['Name'], inline=True)
        embed.add_field(name="Limited", value=read['IsLimited'], inline=True)
        embed.set_footer(text="created: "+str(read['Created']))
        embed.set_thumbnail(url=f"https://www.roblox.com/asset-thumbnail/image?assetId={intem_id}&width=420&height=420&format=png")
        await inter.response.send_message(embed = embed, view=view)
    except:
        embed = disnake.Embed(title=f"AssetId: {intem_id}",description="You AssetId dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='username', description="Search for user roblox")
async def user(inter,user):
    try:
        button = Button(label='Source',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        async def  button_callback(interaction):
            embed = disnake.Embed(title='Json',description=f'```{rbxtrade_userinfo}```', color=disnake.Colour.dark_theme())
            await interaction.response.send_message(embed = embed,ephemeral=True)

        button.callback = button_callback
        request = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}")
        user_result = request.json()
        username_result = user_result['Username']
        rbxtrade = user_result['Id']
        rbxtrade_userinfo = requests.get(f'https://rblx.trade/api/v2/users/{rbxtrade}/info').json()

        if rbxtrade_userinfo['isModerator'] == True:
            status = "✅"
        else: 
            status = "❌"
        embed = disnake.Embed(description=f'**[{username_result}](https://www.roblox.com/users/{rbxtrade}/profile)**', color=disnake.Colour.green())
        embed.add_field(name="UserId", value=rbxtrade_userinfo['userId'] ,inline=True)
        embed.add_field(name="Moderator", value=status, inline=True)
        embed.add_field(name="Trade", value='Rap: {}  \nValue: {} \nRank: {}'.format(rbxtrade_userinfo['accountRAP'],rbxtrade_userinfo['accountValue'],rbxtrade_userinfo['rank']), inline=False)
        embed.set_footer(text="Place visits: "+str(rbxtrade_userinfo['placeVisitCount']))
        embed.set_thumbnail(url="https://www.roblox.com/headshot-thumbnail/image?userId={}&width=420&height=420&format=png".format(user_result['Id']))
        await inter.response.send_message(embed = embed, view=view)
    except:          
        embed = disnake.Embed(title="Username: "+str(user),description="You Username dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='support',description='Send you support')
async def user(inter,text):

    embed2 = disnake.Embed(title=f'Usuario: {inter.author}', description=f'```{text}```', color=disnake.Colour.green())
    embed2.set_image(inter.author.avatar)
    member = bot.owner
    dm = await member.create_dm()
    await dm.send(embed = embed2)
    embed = disnake.Embed(title="Your support has been sent",description=f"Your bug has been successfully reported, thanks for {inter.author} help in our project ❤ \n ```{text}```", color=disnake.Colour.green())
    await inter.response.send_message(embed = embed, ephemeral=True)


@bot.slash_command(name='clothe_id',description='Verify clothe Copyright/Download')
async def user(inter,clothe_id:int):
    try:
        response = requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{clothe_id}")
        template_result = response.json()   
        verify = template_result['IsCopyrightProtected']
        if verify == False:
            embed = disnake.Embed(title=f"Clothe: {clothe_id}",description=f"Status: {verify} \n ``` This clothe can be stolen, copy filter is false```", color=disnake.Colour.green())
            embed.set_thumbnail(url="https://www.roblox.com/asset-thumbnail/image?assetId={}&width=420&height=420&format=png".format(clothe_id))
            embed.add_field(name="Location", value=template_result['location'], inline=False)
            embed.add_field(name="RequestId", value=template_result['requestId'], inline=True)
            embed.add_field(name="Dynamic", value=template_result['IsHashDynamic'], inline=True)
            await inter.response.send_message(embed = embed, ephemeral=False)
        else:
            embed = disnake.Embed(title="Clothe: "+str(clothe_id),description="Copyringht Alert", color=disnake.Colour.red())
            await inter.response.send_message(embed = embed,ephemeral=True)
    except:
        embed = disnake.Embed(title="Clothe: "+str(clothe_id),description="Your Clothe dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='limited_id',description='Search for limiteds')
async def user(inter,limited_id):
    try:
        button = Button(label='Source',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        async def  button_callback(interaction):
            embed = disnake.Embed(title='Json',description=f'```{limited}```', color=disnake.Colour.dark_theme())
            await interaction.response.send_message(embed = embed,ephemeral=True)

        button.callback = button_callback
        limited = requests.get(f'https://rblx.trade/api/v2/catalog/{limited_id}/info').json()
        embed = disnake.Embed(title="Limited: "+str(limited['acronym']),description=limited['description'], color=disnake.Colour.green())
        embed.add_field(name="Demand", value=limited['demand'], inline=True)
        embed.add_field(name="LowestPrice", value=limited['lowestPrice'], inline=True)
        embed.add_field(name="Rare", value=limited['isRare'], inline=True)
        embed.add_field(name="Projected", value=limited['isProjected'], inline=True)
        embed.add_field(name="Value", value=limited['value'], inline=True)
        embed.add_field(name="Rap", value=limited['rap'], inline=True)
        embed.set_footer(text=limited['createdAt'])
        embed.set_thumbnail(url=f"https://www.roblox.com/asset-thumbnail/image?assetId={limited_id}&width=420&height=420&format=png")
        await inter.response.send_message(embed = embed,ephemeral=False, view=view)
    except:
        embed = disnake.Embed(title=f"Limited: {limited_id}",description="Your Limited dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='cookie_checker',description='Search for cookie')
async def user(inter,cookie):
    try:        
        value = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        embed = disnake.Embed(title=value['UserName'], color=disnake.Colour.green())
        if value['IsPremium'] == False:
            status_premium = '❌'
        else:
            status_premium = '✅'
        
        if value['IsAnyBuildersClubMember'] == False:
            status_club = '❌'
        else:
            status_club = '✅'
        thumb = value['ThumbnailUrl']
        thumb_id = value['UserID']
        embed.add_field(name="UserId", value=value['UserID'], inline=True)
        embed.add_field(name="Balance", value=value['RobuxBalance'], inline=True)
        embed.add_field(name="Premium", value=status_premium, inline=False)
        embed.add_field(name="BuildersClub", value=status_club, inline=False)
        embed.add_field(name="Thumbinail", value=f'```{thumb}```', inline=False)
        embed.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={thumb_id}&width=420&height=420&format=png")
        await inter.response.send_message(embed = embed,ephemeral=False)
    except:
        embed = disnake.Embed(title=f"Cookie dont exist...",description=f"````{cookie}```", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='gamepass_id',description='Search for cookie')
async def user(inter,gamepass_id):  
    try:
        button = Button(label='Buy Gamepass',style=disnake.ButtonStyle.green,url=f'https://www.roblox.com/game-pass/{gamepass_id}/myGamePass')
        button2 = Button(label='Source',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button)
        view.add_item(button2)
        async def  button_callback(interaction):
            embed = disnake.Embed(title='Json',description=f'```{gamepass}````', color=disnake.Colour.dark_theme())
            await interaction.response.send_message(embed = embed,ephemeral=True)

        button2.callback = button_callback
        gamepass = requests.get(f'https://api.roblox.com/marketplace/game-pass-product-info?gamePassId={gamepass_id}').json()
        embed = disnake.Embed(title=gamepass['Name'],description=gamepass['Description'], color=disnake.Colour.green())
        embed.add_field(name="Price", value=gamepass['PriceInRobux'], inline=True)
        embed.add_field(name="Sales", value=gamepass['Sales'], inline=True)
        embed.add_field(name="Creator", value=gamepass['Creator']['Name'], inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1013475156464783451/1041780690171220039/unknown.png')
        embed.set_footer(text='Unable to get image')
        await inter.response.send_message(embed = embed,ephemeral=False, view=view)
    except:
        embed = disnake.Embed(title=f"Gamepass: {gamepass_id}",description="Your Gamepass dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)

@bot.slash_command(name='roblox_status',description='RoMonitor status')
async def user(inter):

    embed = disnake.Embed(title=f"Roblox Status",description="", color=disnake.Colour.blue())
    romonitor = requests.get('https://romonitorstats.com/api/v1/stats/platform/get?timestamp=6m').json()
    embed.add_field(name="New 1 week", value='Users: {} \nPlayers: {} \nGroups: {}'.format(romonitor['newUsers'],romonitor['topPlayers'],romonitor['newGroups']), inline=False)
    embed.add_field(name="New 1 Days", value='Users: {} \nPlyers: {} \nGroups: {}'.format(romonitor['newUsersToday'],romonitor['topPlayersToday'],romonitor['newGroupsToday']), inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1013475156464783451/1042225432096952420/unknown.png')
    embed.set_footer(text='Update api: '+str(romonitor['lastCached']))
    await inter.response.send_message(embed = embed,ephemeral=False)


@bot.slash_command(name='server_info',description='server information')
async def user(inter):
    embed = disnake.Embed(title = f"{inter.guild.name}", description = "Information of this Server", color = disnake.Colour.green())
    embed.add_field(name="Server Info", value=f'Server ID: {inter.guild.id}\n Created: {inter.guild.created_at.strftime("%b %d %Y")}\n Owner: {inter.guild.owner.mention}\n Members: {inter.guild.member_count}\n Channels: Text: {len(inter.guild.text_channels)} Voice: {len(inter.guild.voice_channels)}\n Region: {inter.guild.region}\n', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1013475156464783451/1041780690171220039/unknown.png')
    await inter.response.send_message(embed = embed,ephemeral=False)

@bot.slash_command(name='limited_similar',description='server information')
async def gerar(inter, limited_id):
    try:
        button2 = Button(label='Source',style=disnake.ButtonStyle.green)
        view = disnake.ui.View()
        view.add_item(button2)
        async def button_callback(interaction): 
                embed = disnake.Embed(title='Json',description=f'```{response}````', color=disnake.Colour.dark_theme())
                await interaction.response.send_message(embed = embed,ephemeral=True)
        button2.callback = button_callback
        limited_name = requests.get(f'https://rblx.trade/api/v2/catalog/{limited_id}/info').json()
        name = limited_name['acronym']
        response = requests.get(f'https://rblx.trade/api/v2/catalog/{limited_id}/similar').json()
        list = "\n".join(map(lambda x: f"- {x['name']}", response))
        embed = disnake.Embed(title=f"Limiteds Similar {name}: ",description=f"{list}", color=disnake.Colour.green())
        embed.set_thumbnail(url=f"https://www.roblox.com/asset-thumbnail/image?assetId={limited_id}&width=420&height=420&format=png")
        await inter.response.send_message(embed = embed,ephemeral=False, view=view)
    except:
        embed = disnake.Embed(title=f"Gamepass: {limited_id}",description="Your Limited dont exist...", color=disnake.Colour.red())
        embed.set_footer(text='Request /support')
        await inter.response.send_message(embed = embed,ephemeral=True)



@bot.event
async def on_ready():
    activity = disnake.Game(name=f"/help  |  {round(bot.latency * 1000)}ms", type=3)
    await bot.change_presence(status=disnake.Status.idle, activity=activity)

bot.run('TOKEN')

