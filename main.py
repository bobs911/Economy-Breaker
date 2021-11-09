import os
import time
import sys
import random

#thecolors = {
#  Blue:"\033[0;34m",
#  Cyan:"\033[1;36m",
#  White:"\033[0;37m", 
#  Green:"\033[0;32m",
#  Orange:"\033[0;33m",
#  Pink:"\033[1;31m"
#  }

Blue="\033[0;34m"
Cyan="\033[1;36m"
White="\033[0;37m" 
Green="\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"

def ScrollTxt(text):
  for char in text:
    mydelay=random.randint(1,5)
    mydelay = mydelay/100
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(mydelay)

def intro():
	ScrollTxt(Pink + "WELCOME TO UNIVERSE ECONOMY!")
	ScrollTxt(Blue + "In this game you will take over the universe and create your own supreme EMPIRE.")



