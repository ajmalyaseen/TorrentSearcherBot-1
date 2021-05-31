from pyrogram import Client, filters
from translation import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery




@Client.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
            InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
        ],[
            InlineKeyboardButton("📕ABOUT", callback_data= "about"),
            InlineKeyboardButton("🔐 CLOSE", callback_data= "close")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    


    elif query_data == "about": 
        buttons = [[
            InlineKeyboardButton('⬇️BACK', callback_data='start'),
            InlineKeyboardButton('🔐CLOSE', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()
        
        
