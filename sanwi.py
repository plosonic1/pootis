import discord
import os
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'soy {bot.user} y odio a todos')
@bot.command()
async def mem(ctx):
    with open('edit durisimo de tenchingan/a.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def mem2(ctx):
    with open('edit durisimo de tenchingan/b.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def me(ctx):
    await ctx.send(f'eres un completo inutil bueno para nada, que dios no te bendiga')
@bot.command()
async def chiste(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=xvFZjo5PgG0')
@bot.command()
async def pootis(ctx):
    await ctx.send(f"im cuming")

# Nuevo Comando: tf2character
@bot.command()
async def tf2(ctx):
    '''Envía información aleatoria de personajes de TF2'''
    characters = [
        "Scout: 'Grass grows, birds fly, sun shines, and brotha'... I hurt people.'",
        "Soldier: 'If fighting is sure to result in victory, then you must fight!'",
        "Pyro: *muffled laughter and fire sounds*",
        "Demoman: 'KA-BOOM! Kaboom to you, sir!'",
        "Heavy: 'I am Heavy Weapons Guy, and this is my weapon.'",
        "Engineer: 'Erectin' a dispenser!'",
        "Medic: 'Prepare for your examination!'",
        "Sniper: 'Boom. Headshot.'",
        "Spy: 'Gentlemen...'"
    ]
    await ctx.send(random.choice(characters))
@bot.command()
async def weapon(ctx):
    '''Envía información aleatoria sobre las armas de TF2'''
    weapons = [
        "Scattergun: La mejor amiga del Scout, perfecta para el combate a corta distancia. ¡BANG, BANG!",
        "Rocket Launcher: El arma favorita del Soldier. ¿Matar enemigos? ¿Propulsarte a ti mismo? ¡Todo en uno!",
        "Flamethrower: ¿A quién no le gusta prender fuego a todo con el Pyro? Por cierto, ¿qué dice el Pyro? Nadie lo sabe.",
        "Stickybomb Launcher: Ideal para trampas explosivas. ¡Kaboom, mi amigo Demoman!",
        "Minigun (Sasha): El Heavy nunca deja de presumir de ella. '¡Ella dispara 10,000 balas por segundo!'",
        "Wrench: La llave del Engineer no solo construye cosas, también es excelente para aplastar Spies.",
        "Medi Gun: No es un arma, pero el Medic la usa para mantener al equipo vivo. ¡Ubercharged!",
        "Sniper Rifle: El arma del Sniper. ¡Boom, headshot!",
        "Knife: El Spy y su legendaria puñalada por la espalda. 'Messieurs, adiós.'"
    ]
    await ctx.send(random.choice(weapons))


bot.run('aqui va el token ese')
