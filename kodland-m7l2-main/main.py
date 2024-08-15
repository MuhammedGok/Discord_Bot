import discord
from discord.ext import commands
from model import get_class
import requests
import os
import random
from bot_mantik import *


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

dil="en"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def set_language(ctx, language):
    global dil
    if language in ['en', 'tr']:
        dil = language
        await ctx.send(f"Dil değiştirildi: {dil}")
        await ctx.send(f"Language changed: {dil}")
    else:
        await ctx.send("Geçersiz dil. Lütfen 'en' veya 'tr' kullanın")
        await ctx.send("Invalid language. Please use 'en' or 'tr'")










def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']












#dört işlem 


@bot.command()
async def toplama(ctx, sayi1: int, sayi2: int):
    if dil == "tr":
        await ctx.send(sayi1 + sayi2)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")


@bot.command()
async def çıkarma(ctx, sayi1: int, sayi2: int):
    if dil == "tr":
        await ctx.send(sayi1-sayi2)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")


@bot.command()
async def çarpma(ctx, sayi1: int, sayi2: int):
    if dil == "tr":
        await ctx.send(sayi1*sayi2)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")


@bot.command()
async def bölme(ctx, sayi1: int, sayi2: int):
    if dil == "tr":
        await ctx.send(sayi1/sayi2)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")



    #üs 


@bot.command()
async def üs(ctx, sayi1: int, sayi2: int):
    if dil == "tr":
        await ctx.send(sayi1**sayi2)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")




    #mem

@bot.command()
async def mem_mc(ctx):
    resimler_listesi = os.listdir("images")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'images/{rastgele_resim}', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)



@bot.command()
async def mem_gow(ctx):
    resimler_listesi3 = os.listdir("images3")
    rastgele_resim3 = random.choice(resimler_listesi3)
    with open(f'images3/{rastgele_resim3}', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)


@bot.command()
async def hayırlı_cumalar(ctx):
    if dil == "tr":
        resimler_listesi4 = os.listdir("HayırlıCumalar")
        rastgele_resim4 = random.choice(resimler_listesi4)
        with open(f'HayırlıCumalar/{rastgele_resim4}', 'rb') as f:
                # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
        # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")



@bot.command()
async def SA(ctx):
    if dil == "tr":
        await ctx.send("AS")
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")



@bot.command()
async def Karizma(ctx):
    if dil == "tr":
        await ctx.send("https://tenor.com/view/erdo%C4%9Fan-gif-15666252741524182242")
        await ctx.send("(!)")
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")








@bot.command()
async def emoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def para(ctx):
    if dil == "tr":
        await ctx.send(yazi_tura())
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")





@bot.command()
async def ördek(ctx):
    if dil == "tr":
        image_url = get_duck_image_url()
        await ctx.send(image_url)
    elif dil == "en":
        await ctx.send("the command you wrote belongs to a different language")



@bot.command()
async def check(ctx):
        if ctx.message.attachments:
            for attachment in ctx.message.attachments:
                await attachment.save(f"./{attachment.filename}")
                await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
        else:
            if dil == "tr":
                await ctx.send("Resim yüklemeyi unuttun!")
            elif dil == "en":
                await ctx.send("You forgot to upload a picture!")




@bot.command()
async def yardım(ctx):
        if dil == "tr":
            await ctx.send("Komutlar")
            await ctx.send("/toplama sayı1 sayı2 : toplama işlemini yapar")  #Kendime not buraya tüm komutları ekle
            await ctx.send("/çıkarma sayı1 sayı2 : çıkarma işlemini yapar")
            await ctx.send("/çarpma sayı1 sayı2 : çarpma işlemini yapar")
            await ctx.send("/bölme sayı1 sayı2 : bölme işlemini yapar")
            await ctx.send("/üs sayı1 sayı2  : sayı1 taban sayı2 kuvvet olduğunda sonucun ne olduğunu yazar.")
            await ctx.send("/mem_mc : Minecraft ile ilgili rastgele bir mem atar")
            await ctx.send("/mem_gow : God of War ile ilgili rastgele bir mem atar")
            await ctx.send("/hayırlı_cumalar : Rastgele bir hayırlı cumalar mesajı atar")
            await ctx.send("/ördek : Rastgele bir ördek fotoğrafı atar")
            await ctx.send("/SA : Selama karşılık verir SHSJSHSJJS")
            await ctx.send("/emoji : Rastgele bir emoji atar")
            await ctx.send("/para : Yazı tura atar")
            await ctx.send("/check : Minecraftla ilgili bir görsel yüklediğinde onun hangi Boyutta olduğunu söyler")
            await ctx.send("/Karizma : Karizmanın vücut bulmuş halini atar (!)")
        elif dil == "en":
            await ctx.send("the command you wrote belongs to a different language")            



    #dört işlem 


@bot.command()
async def addition(ctx, number1: int, number2: int):
    if dil == "en":
        await ctx.send(number1 + number2)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")


@bot.command()
async def subtraction(ctx, number1: int, number2: int):
    if dil == "en":
        await ctx.send(number1-number2)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")


@bot.command()
async def multiplication(ctx, number1: int, number2: int):
    if dil == "en":
        await ctx.send(number1*number2)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")

@bot.command()
async def division(ctx, number1: int, number2: int):
    if dil == "en":
        await ctx.send(number1/number2)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")


    #üs 


@bot.command()
async def exponent_operation(ctx, number1: int, number2: int):
    if dil == "en":
        await ctx.send(number1**number2)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")











@bot.command()
async def Hello(ctx):
    if dil == "en":
        await ctx.send("Hi")
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")




@bot.command()
async def Cool(ctx):
    if dil == "en":
        await ctx.send("https://tenor.com/view/erdo%C4%9Fan-gif-15666252741524182242")
        await ctx.send("(!)")
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")








@bot.command()
async def coin(ctx):
    if dil == "en":
        await ctx.send(yazi_tura())
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")



@bot.command()
async def duck(ctx):
    if dil == "en":
        image_url = get_duck_image_url()
        await ctx.send(image_url)
    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")






@bot.command()
async def assistance(ctx):
    if dil == "en":
        await ctx.send("Commands")
        await ctx.send("/addition number1 number2 : performs the addition operation")
        await ctx.send("/subtraction number1 number2 : performs subtraction")
        await ctx.send("/multiplication number1 number2 : performs multiplication")
        await ctx.send("/division number1 number2 : performs division")
        await ctx.send("/exponent_operation number1 number2 : writes what the result is when number1 is base number2 power")
        await ctx.send("/mem_mc : Throws a random meme related to Minecraft")
        await ctx.send("/mem_gow : Throws a random meme related to God of War")
        await ctx.send("/duck : Randomly assigns a photo of a duck")
        await ctx.send("/Hello : Returns the greeting")
        await ctx.send("/emoji : Throws a random emoji")
        await ctx.send("/coin : He flips a coin")
        await ctx.send("/check : When you upload an image related to Minecraft, it tells you which dimension it belongs to")
        await ctx.send("/Cool : Throws the embodiment of coolness (!)")

    elif dil == "tr":
        await ctx.send("Yazdığınız komut başka bir dile ait")







bot.run('TOKEN')
