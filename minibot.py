import discord
import responses
import random


def run_discord_bot():
    TOKEN = 'MTEwMTkwNTYxMTQyOTUxOTUzMw.GtKWam.R6_LJhhgejLfdMfwl2OLaiZdXPpS-TEMvWhyK0'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

### Roll [n] Die ###
    async def roll_dice(message):
        try:
            command, argument = message.content.split(" ")
            n = int(argument)
            result = random.randint(1, n)
            return f"The result of rolling a {n}-sided dice is {result}."
        except ValueError:
            return "Please provide a valid number."
        except:
            return "Oops! Something went wrong."
        
    # Define the roll command for the Discord bot
    @client.event
    async def on_message(message):
        if message.content.startswith("!roll"):
            result = await roll_dice(message)
            await message.channel.send(result)
    # Define the command to shut down the bot
    @client.event
    async def on_message(message):
        if message.content == "!shutdown":
            await message.channel.send("Shutting down the bot...")
            await client.close()

    client.run(TOKEN)