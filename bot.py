import discord
from discord.ext import commands
import asyncio
from skin_scraper import SkinScraper
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

skin_scraper = SkinScraper()

@bot.event
async def on_ready():
    print(f'{bot.user} è online!')
    await bot.change_presence(activity=discord.Game(name='Cerca skin OW | !skin help'))

@bot.command(name='skin')
async def search_skin(ctx, *, query=None):
    """Cerca i codici delle skin di Overwatch"""
    if query is None:
        embed = discord.Embed(title='🎮 Overwatch Skin Bot', color=discord.Color.orange())
        embed.add_field(name='Comandi disponibili:', value=
            '`!skin <nome_hero>` - Cerca skin per eroe\n'
            '`!skin all` - Mostra tutte le skin recenti\n'
            '`!skin legendary` - Solo skin leggendarie\n'
            '`!skin update` - Aggiorna il database\n'
            '`!skin help` - Mostra questo messaggio',
            inline=False)
        await ctx.send(embed=embed)
        return
    
    if query.lower() == 'help':
        embed = discord.Embed(title='🎮 Overwatch Skin Bot - Aiuto', color=discord.Color.orange())
        embed.add_field(name='Come usare:', value=
            'Digita `!skin [nome_hero]` per cercare skin\n\n'
            '**Eroi supportati:**\n'
            'Tracer, Genji, Reinhardt, D.Va, Mercy, Widowmaker, Bastion, Soraka, Torbjorn, Ana, Lucio, Mei, Zenyatta, '
            'Soldier76, McCree, Junkrat, Winston, Symmetra, Hanzo, Roadhog, Pharah, etc.',
            inline=False)
        embed.add_field(name='Filtri:', value='`!skin legendary` - Solo leggendarie\n`!skin epic` - Solo epiche\n`!skin all` - Tutte le skin',
            inline=False)
        await ctx.send(embed=embed)
        return
    
    async with ctx.typing():
        try:
            skins = await skin_scraper.search_skins(query)
            
            if not skins:
                await ctx.send(f'❌ Nessuna skin trovata per: {query}')
                return
            
            for skin in skins:
                embed = discord.Embed(
                    title=f"🎨 {skin['nome']}",
                    description=f"**Eroe:** {skin['eroe']}\n**Rarità:** {skin['rarità']}",
                    color=discord.Color.orange()
                )
                embed.add_field(name='Codice:', value=f'```{skin["codice"]}```', inline=False)
                embed.add_field(name='Fonte:', value=skin['fonte'], inline=False)
                embed.add_field(name='Data:', value=skin['data'], inline=False)
                embed.set_footer(text='Aggiornato al 100% | Reddit + Blizzard + Official Sources')
                await ctx.send(embed=embed)
        
        except Exception as e:
            await ctx.send(f'❌ Errore nella ricerca: {str(e)}')

@bot.command(name='update')
async def update_skins(ctx):
    """Aggiorna il database delle skin"""
    async with ctx.typing():
        await skin_scraper.update_all_sources()
        await ctx.send('✅ Database aggiornato dalle fonti ufficiali!')

bot.run(os.getenv('DISCORD_TOKEN'))