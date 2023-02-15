from config import *
from aiogram import *
from Parsers import *
import datetime
import asyncio
bot = Bot(token)
dp=Dispatcher(bot)
@dp.message_handler()
async def massege_hook(message:types.Message):
    if message.text.count("instagram")!=0:
        media = types.MediaGroup()
        file_list=InstaParse.DownloadfrInstagram(message)
        for file in file_list:
            if file["isPhoto"]=="True":
                media.attach_photo(types.InputFile(file["url"]),"")
            else:
                media.attach_video(types.InputFile(file["url"]),"")
        
        await message.reply_media_group(media)
        return InstaParse.CoverTracks(str(message.message_id))

    if message.text.count("tiktok")!=0:
        print(message)
        await bot.send_video(video=TTParse.DownloadfrTikTok(message.text),chat_id=message.chat.id,reply_to_message_id=message.message_id)

@dp.message_handler(commands=["start"])
async def begin(message:types.Message):
    await bot.send_message(message.chat.id,"Добридень,це бот котрий належить группі 'Курилка 3.0',якщо ви не належите до учасників даного товариства попрошу вас обмежити використання бота завантаження постів з instagram та TikTok. Дякую за розуміння \n Skrynka")


async def birtdaysss(birtday):
    pass

async def on_startip(dp):
    bot.send_message("Привіт папуг")
    asyncio.create_task(birtdaysss())

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)