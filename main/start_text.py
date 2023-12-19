from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is personal use bot 🙏. Do you want your own bot? 👇 Click the source code to deploy"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SOURCE CODE", url="https://t.me/+VhJIV2F3RxljNTNl")
        ],[
        InlineKeyboardButton("🖥️ How To Deploy", url="https://t.me/+VhJIV2F3RxljNTNl")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"ʜᴇʏ {msg.from_user.mention} 👋🏻 ɪ ᴀᴍ ꜱɪᴍᴘʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀꜱᴏɴʟ ᴜꜱᴀɢᴇ♻️. 
\nᴊᴜꜱᴛ ꜱᴇɴᴅ ᴀ ꜰɪʟᴇ ᴀɴᴅ ᴍᴇɴᴛɪᴏɴ ꜰɪʟᴇ /rename YOUR FILE NAME 
\nɴᴏᴡ ʏᴏᴜʀ ꜰɪʟᴇ ɪꜱ ʀᴇɴᴀᴍᴇ👍🏻

\n👨🏻‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ: <b><a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a></b>

\n©ᵖᵒʷᵉʳᵉᵈ ᵇʸ <b><a href=https://telegram.me/CK4U2>CK4U2</a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/CK4U2")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/KING_WMP>Chethmina Kavishan</a>"  
    Source="<a href=https://t.me/+VhJIV2F3RxljNTNl>Click Here</a>"
    txt=f"<b>🤖ᴍʏ ɴᴀᴍᴇ: {me.mention}\n👨🏻‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a>\n📢ᴜᴘᴅᴀᴛᴇꜱ: <a href=https://t.me/CK4U2>CK4U2</a>\n🔮ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


