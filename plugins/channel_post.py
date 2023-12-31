import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import aiohttp
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ForceReply
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from pathlib import Path
import requests
import string
import re

##################### FOR VIDEO SPLITTER ########################
import subprocess
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper_func import progress_for_pyrogram
#from helper.database import db
from asyncio import sleep
#from PIL import Image
import os, time

##################### FOR JIO CENIMA DOWNLOAD ########################
# import subprocess
# import jwt
# import json
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

##################### FOR WEB SCRAPPING ########################
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService

m3u8DL_RE = 'N_m3u8DL-RE'

def replace_invalid_chars(title: str) -> str:
    invalid_chars = {'<': '\u02c2', '>': '\u02c3',
    ':': '\u02d0', '"': '\u02ba', '/': '\u2044',
    '\\': '\u29f9', '|': '\u01c0', '?': '\u0294',
    '*': '\u2217'}
    
    return ''.join(invalid_chars.get(c, c) for c in title)
    

def get_accesstoken():
            IdURL = "https://cs-jv.voot.com/clickstream/v1/get-id"
            GuestURL = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"
            id = requests.get(url=IdURL).json()['id']
        
            token = requests.post(url=GuestURL, json={
                    'adId': id,
                    "appName": "RJIL_JioCinema",
                    "appVersion": "23.10.13.0-841c2bc7",
                    "deviceId": id,
                    "deviceType": "phone",
                    "freshLaunch": True,
                    "os": "ios"
                }, headers={
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                }).json()
    
            return token["authToken"],token["deviceId"]
    
    
@Bot.on_message(filters.command('start') & filters.private )
async def start_command(client: Client, message: Message):
    await message.reply_text("hello buddy ......",quote=True)
        
@Client.on_message(filters.private & filters.video)
async def doc(bot, update):
    file = getattr(update, update.media.value)
    filename = file.file_name
    output_folder = f"downloads/{file.file_name.split('_')[0]}/Parts"
    os.makedirs(output_folder)
    logger.info(f"folder :-{output_folder} ")
    #output_folder = path = os.path.join(f"downloads/{file.file_name.split('_')[0]}/Parts")
    
    file_path = f"downloads/{file.file_name.split('_')[0]}/{file.file_name.split('.')[0]}.mp4"
    logger.info(file_path)
    main_folder = f"downloads/{file.file_name.split('_')[0]}"
    video_len = file.file_size
    parts = 2
    if file.file_size > 2000 * 1024 * 1024:
         return await update.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    ms =   await update.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....") 
    
    try:
       logger.info('starting download')
       path = await bot.download_media(message=update, file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time())) 
       #path = await bot.download_media(message=update, file_name=file_path) 
    except Exception as e:
     	return await ms.edit(e)
    logger.info('download complete')	     
    duration = 0
    await ms.edit(text="DL complete")
    
    ffmpeg = "./ffmpeg.exe"
    if os.path.isfile(file_path):
        logger.info("no issues")
        await ms.edit(text="starting to split")
        parts = 4
        acodec="copy"
        vcodec="copy"
        extra=""
        
        cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file_path}"
        video_length = float(subprocess.check_output(cmd, shell=True))
        logger.info("Video length in seconds: " + str(video_length))
        duration_per_part = video_length / parts
        logger.info("duration_per_part: " + str(duration_per_part))
        #try:
        for i in range(parts):
            logger.info("split start")
            start_time = i * duration_per_part
            logger.info(f"start_time :- {start_time}")
            output_file = os.path.join(output_folder, f"{file.file_name.split('_')[0]}_part_{i+1:02d}.mp4")
            logger.info(f"output_file dire :-{output_file} ")
            cmd = f"ffmpeg -i {file_path} -ss {start_time} -t {duration_per_part} -c copy {output_file}"
            output_parts = f'{file.file_name.split("_")[0]}_part_{i+1:02d}.mp4'
            subprocess.check_output(cmd, shell=True)
            await bot.send_video(
                        chat_id=update.chat.id,
                        video=output_file,
                        caption=output_parts,
                        supports_streaming=True,
                        )
        shutil.rmtree(main_folder)
            
    else:
        logger.info("issues found, passing to sub process")
        await ms.edit(text="process excuted somthing wrong")
