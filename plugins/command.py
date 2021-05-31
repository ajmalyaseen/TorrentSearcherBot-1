#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from translation import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    buttons = [[
        InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
        InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
        ],[
        InlineKeyboardButton("📕ABOUT", callback_data= "about"),
        InlineKeyboardButton("🔐 CLOSE", callback_data= "close")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)

    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
    
    
@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('⬇️BACK', callback_data='start'),
        InlineKeyboardButton('🔐CLOSE', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


    
