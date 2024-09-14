import requests
import json
import hashlib
import os
import colorama
from colorama import Fore,Style

# some decorations for giving it a good look and feel.
colorama.init()
print(Fore.RED + Style.BRIGHT)
print()
print(r" ██╗██████╗ ")
print(r" ██║██╔══██╗            IP-TRACER        ")
print(r" ██║██████╔╝     »»»Author:White_Devi««« ")
print(r" ██║██╔═══╝             ꧁ᬊᬁᴀɴɢᴇʟᬊ᭄꧂ツ           ")
print(r" ██║██║       Instagram ID:@Whitedevil1097  ")
print(r" ╚═╝╚═╝       Youtube Channel:Hacker_Devill")
print( "                   🦋⃟ᴠͥɪͣᴘͫ•𝆺𝅥❤️<200d>🔥😈𓆩ꨄ︎𓆪  ")
print(r"IP-VS1.0 ")
def get_ip_location():
    response = requests.get('https://ipapi.co/json/')
    data = json.loads(response.text)
    return f"IP: {data['ip']}\nLocation: {data['city']}, {data['region']}, {data['country_name']} ({data['latitude']}, {data['longitude']})"
print(get_ip_location())
print('              😎 You Have Been Hacked 😎 ')
print('👾 Send 1 BTC Crypto In My Wallet,💀 if you dont send me you shoud be punshed💀')
print('👽 Your System Is Compromise 👽𓆣 Your Private Data Can Request to Download👽𓆣💥')
print('             BokaChoda = 🦋⃟ᴠͥɪͣᴘͫ•𝆺𝅥❤️<200d>🔥😈𓆩ꨄ︎𓆪')                                

