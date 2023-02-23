from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
response = bot.ask("Hello world!")
bot.delete_conversation()
print(response)