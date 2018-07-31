# -*- coding: utf-8 -*-
# MEMENTO MORIBOT: an emoji tweetbot
# inspired by Parker Higgins' Choochoobot 
# https://github.com/thisisparker/choochoobot

import numpy as np
import random
import re
import sys
import twitter
from local_settings import *

MORI_TILES = [u"💀", u"🐚", u"👑",
              u"🌹", u"⏳", u"⚱️",
              u"🕯", u"📚", u"🕰",
              u"🍷", u"🎻", u"🍇",
              u"⚰️"]
MOON_TILES = ["🌑", "🌒", "🌔",
              "🌕", "🌖", "🌘"]

def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api


def fill_row():
    length = 20
    item_rarity = 10
    row = ""
    space_char = " "

    for spot in range(length):
        tile = np.random.randint(1, item_rarity)
        if tile == 1:
            row += random.choice(MORI_TILES)
        else:
            row += space_char
    return row


def generate_scene():
    height = 4
    tweet = ""
    scene = []
    check = 0

    while check == 0:
        for line in range(height):
            scene.append(fill_row())

        tweet += scene[0] + "\n" + \
                 scene[1] + "\n" + \
                 scene[2] + "\n" + \
                 scene[3]
        match = re.findall("💀", tweet)
        if len(match) > 0:
            check += 1
        else:
            tweet = ""
            scene = []
    return tweet

if __name__=="__main__":
    guess = 0
    if DEBUG == False:
        guess = np.random.randint(0, ODDS)
        if guess == 0
            api = connect()
            new_tweet = generate_scene()
            api.PostUpdate(status=new_tweet)
            print(new_tweet.encode('utf-8'))
        else:
            print("Not this time, buddy.")
    else:
        print("DEBUG MODE: TEST OUTPUT" + "\n" + new_tweet.encode('utf-8'))
