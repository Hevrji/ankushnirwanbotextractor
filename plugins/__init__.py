from pyrogram import filters
from pyrogram import Client as stark
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys


@stark.on_message(filters.command("start") & filters.edit)
async def Start_msg(bot: stark , m: Message):
    # Your existing code here

    await bot.send_photo(
    m.chat.id,
    photo="https://graph.org/file/51006f3a1cb6eb81fe55f.jpg",
    caption = "** Hii I AM Ankush Batch Extract Bot**.\n"
                            "Press **Menu Command To Use Our Bot**..\n\n"
                            "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : @ankushnirwan**")
           


@stark.on_message(filters.command(["restart"]) & ~filters.edited)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@stark.on_message(filters.command(["log"]) & ~filters.edited)
async def log_msg(bot: stark , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
