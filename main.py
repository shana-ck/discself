import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD')
USER_ID = os.getenv('USER_ID')

guild_subscription_options = discord.GuildSubscriptionOptions.off()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('----')

    async def on_message(self, message):
        if message.author.id == USER_ID:
            with open('logger.txt', 'a') as file:
                file.write(f'{message.author.id}: {message.content}\n')
            return


print("starting...")
client = MyClient()
client.run(TOKEN)
