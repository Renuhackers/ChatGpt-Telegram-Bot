from pyrogram import Client as neural ,filters
from helpers.buttons import *
@neural.on_message( filters.command("start"))
async def start(bot, msg):
    markup = InlineKeyboardMarkup([[channel, group], [developer,help]])
    await msg.reply(f"**Hello {msg.from_user.first_name} This Bot is Successfully Hacked by Renus Hacker.join our channels for learn hacking.\nThis is phishing bot but now it's chat got bot 😈**",
    reply_markup= markup )
