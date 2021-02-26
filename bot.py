import discord
# import scrython
from discord.ext import commands
from funcoes import dado, convert_usd, convert_ars
from chave import key

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    print('It just works!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def usd(ctx, valor):
    RS = convert_usd(valor)
    print('usd')
    await ctx.send(f'```💵 USD: {valor} Dólares → R$ {RS:.2f}```')

@client.command()
async def ars(ctx, valor):
    RS = convert_ars(valor)
    print('ars')
    await ctx.send(f'```💷 ARS: {valor} → R$ {RS:.2f}```')

@client.command(aliases=['d','dado','rolar'])
async def r(ctx,x='1d20'):
    v, t = dado(x)
    print('dado')
    await ctx.send(f'```{x} 🎲\nResultado: {v} \nTotal: {t}```')

@client.command()
async def clear(ctx, q=0):
    print('clear')
    await ctx.channel.purge(limit=q+1)

@client.command()
async def playlist(ctx):
    print('playlist')
    await ctx.send('```https://youtu.be.com/playlist?list=PL_n-5o0eUj7BWesD5NEfPvIH2_FM1t9lW```')

@client.command()
async def help(ctx):
    print('help')
    await ctx.send(f'```Comandos: \n\n ars <valor em pesos> - converte ARS em BRL. \n usd <valor em dólares> - Converte USD em BRL. \n r <XdY> - rola um XdY dado, X quantidade de dados, Y número de faces, se nada for informado, rola 1d20. \n clear <quantidade de mensagens para apagar> - apaga a quantidade de mensagens. \n ping - testa a latência do bot.```')

@client.command(aliases=['cmd','commander','comandante'])
async def edh(ctx, cor = None, cmc = None):
    print('edh')
    s = 'https://scryfall.com/random?q=is:commander'
    cr = '+c='
    cm = '+cmc='

    if cor != None:
        s = s + cr + str(cor)

    if cmc != None:
        s = s + cm + str(cmc)

    if (cor == None) and (cmc == None):
        await ctx.send(f'https://edhrec.com/random')
    else:
        await ctx.send(s)

@client.command()
async def git(ctx):
    print('git')
    await ctx.send('```https://github.com/bruhensant/BotHen```')

client.run(key)