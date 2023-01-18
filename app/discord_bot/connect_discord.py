# Import the required libraries and modules
from dotenv import load_dotenv  # dotenv module allows us to access environment variables stored in a .env file
import discord  # library for interacting with the Discord API
import os  # provides functions for interacting with the operating system

# Import the chatgpt_response function from the connect_openai module
from app.openai_api.connect_openai import chatgpt_response

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the Discord API token from the environment variables
discord_token = os.getenv("DISCORD_TOKEN")

# Check if the currency_converter directory is in the app directory
project_directory = os.listdir("app")
if "currency_converter" in project_directory:
    # If it is, import the converter function from the converter module
    from app.currency_converter.converter import converter

# Define the MyClient class, which is a subclass of discord.Client
class MyClient(discord.Client):
    # Define the on_ready event, which is triggered when the client is successfully connected to the Discord API
    async def on_ready(self):
        print("Logged on as: ", self.user)

    # Define the on_message event, which is triggered when a message is received by the client
    async def on_message(self, message):
        print(message.content)  # print the content of the message to the console
        # Check if the message was sent by the client itself
        # don't respond to ourselves
        if message.author == self.user:
            return
        command, refine_message=None, None

        # Check if the message starts with any of the following commands: '/help', '/?', '/ai', '/cc'
        for feature in ['/help','/?','/ai', '/cc']:
            if message.content.startswith(feature):
                # If it does, split the message into the command and the message to be processed
                command=message.content.split(' ')[0]
                refine_message=message.content.replace(feature, '')
                print(command, refine_message)

        # If the command is '/help' or '/?'
        if command == '/help' or command == '/?':
            # Send a message to the channel with a list of available commands
            await message.channel.send("""/ai: Access chatgpt features.""")

        # If the command is '/ai'
        if command == '/ai':
            # Call the chatgpt_response function with the refine_message as the prompt
            # Assign the response to the ai_response variable
            ai_response = chatgpt_response(prompt=refine_message)
            # Send a message to the channel with the original message and the AI response
            await message.channel.send(f"You said: {refine_message} {ai_response}")

# Set the intents for the client to the default intents, with message content enabled
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the MyClient class with the specified intents
client = MyClient(intents=intents)
