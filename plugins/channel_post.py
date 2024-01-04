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
import subprocess
import jwt
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
        
@Bot.on_message(filters.command('token') & filters.private )
async def start_command(client: Client, message: Message):
    
    IdURL = "https://cs-jv.voot.com/clickstream/v1/get-id"
    GuestURL = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"
    id = requests.get(url=IdURL).json()['id']
    token = requests.post(url=GuestURL, json={
                                              'adId': id,
                                              "appName": "RJIL_JioCinema",
                                              "appVersion": "23.10.13.0-841c2bc7",
                                              "deviceId": id,
                                              "deviceTawait imog.edit(text=response2)ype": "web",
                                              "freshLaunch": True,
                                              "os": "ios"
                                          }, headers={
                                              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                                          }).json()

    tkn = token
    bot_msg = await message.reply_text(tkn, quote = True)


@Client.on_message(filters.private & filters.regex(pattern=".*http.*"))
async def echo(bot, update):
        imog = await update.reply_text("<b>Processing... ⏳</b>",)
        link = update.text
        link_id = re.findall(r'.*/(.*)', link)[0].strip()
        h = await update.reply_text(f"getting token")
        access_token = get_accesstoken()[0]
        await h.edit(text="token recived")
        header_data = jwt.get_unverified_header(access_token)
        decoded = jwt.decode(access_token, algorithms=["HS512", "HS256"], options={"verify_signature": False})
        deviceId = decoded['data']['deviceId']
        uniqueid = decoded['data']['userId']
        appName = decoded['data']['appName']
        await h.edit(text=f"{decoded}\n\n{header_data}\n\n{deviceId}\n{uniqueid}\n{appName}")
        headers2 = {
            'authority': 'apis-jiovoot.voot.com',
            'accept': 'application/json, text/plain, */*',
            'accesstoken': access_token,
            'appname': "RJIL_JioCinema",
            'content-type': 'application/json',
            'deviceid': get_accesstoken()[1],
            'origin': 'https://www.jiocinema.com',
            'referer': 'https://www.jiocinema.com/',
            'uniqueid': uniqueid,
            'user-agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'versioncode': '2312070',
            'x-platform': 'androidweb',
            'x-platform-token': 'web',
        }

        json_data2 = {
            '4k': False,
            'ageGroup': '18+',
            'appVersion': '3.4.0',
            'bitrateProfile': 'xhdpi',
            'capability': {
                'drmCapability': {
                    'aesSupport': 'yes',
                    'fairPlayDrmSupport': 'yes',
                    'playreadyDrmSupport': 'none',
                    'widevineDRMSupport': 'yes',
                },
                'frameRateCapability': [
                    {
                        'frameRateSupport': '30fps',
                        'videoQuality': '1440p',
                    },
                ],
            },
            'continueWatchingRequired': True,
            'dolby': False,
            'downloadRequest': False,
            'hevc': False,
            'kidsSafe': False,
            'manufacturer': 'Windows',
            'model': 'Windows',
            'multiAudioRequired': True,
            'osVersion': '10',
            'parentalPinValid': True,
        }
        await update.reply_text("requsting DATA",)
        response2 = requests.post('https://apis-jiovoot.voot.com/playbackjv/v4/'+link_id+'', headers=headers2, json=json_data2, verify=False).json()
        contentType = response2
        await imog.edit(text=response2)

