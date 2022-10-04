import discord
from discord import app_commands
from discord import message
import os
from webserver import keep_alive
import csv

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 924742107661492254))
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "whitelist", description = "Add your 0x to the whitelist", guild = discord.Object(id = 924742107661492254))
async def self(interaction: discord.Interaction,number: str):
    name = interaction.user.id
    input = [name,number]
    duplicate = False
    with open ('data.csv', 'r+') as file:
      
      reader = csv.reader(file, delimiter=',')
      for row in reader:
        print(name, row[0])
        if str(name) == row[0]:
          await interaction.response.send_message("Your wallet is already set")
          return None
      writer = csv.writer(file)
      writer.writerow(input)
      print("New entry added")
      await interaction.response.send_message("Your wallet has been added!")


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)
