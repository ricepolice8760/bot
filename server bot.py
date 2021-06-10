import discord, asyncio, random


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("게임")
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message, discord=None):

    if message.content.startswith("랜덤"):
        for i in range(1, 20):
            await message.channel.send(random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'H', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]))

client.run("ODUyMTkzNzI2NTIzNTA2NzA4.YMDRQQ.1VtBhI9e-ijcbNJK_yBmLee5vDM")