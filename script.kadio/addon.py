import xbmcaddon
import xbmcgui
import subprocess
import sys
import xbmc
import time
import os.path
from os import path
audiof = '/tmp/radio.wav'
if path.exists('/usr/bin/rtl_fm') == False:
    subprocess.call("yes | sudo apt install rtl-sdr sox", shell=True)
subprocess.call("sudo pkill -9 rtl_fm; sudo pkill -9 sox; sudo rm -f " + audiof, shell=True)
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
startcastmsg = "Tuning to configured FM frequency "
stopcastmsg = "Shutting down radio..."
station = xbmcgui.Dialog().input("FM Base Station Number", type=xbmcgui.INPUT_NUMERIC)
decimal = xbmcgui.Dialog().input("FM Decimal Station", type=xbmcgui.INPUT_NUMERIC)
startcastmsg = startcastmsg + station + "." + decimal
cmd = "sudo rtl_fm -g 50 -f " + station + "." + decimal + "M -M wbfm | sox -t raw -r 16k -e signed -b 16 -c 1  - " + audiof + " &"
subprocess.call('/usr/bin/watch -n 500 rm /tmp/radio.wav &', shell=True)

subprocess.call(cmd, shell=True)

time.sleep(2)
try:
    f = open(audiof)
    xbmc.Player().play(audiof)
    xbmcgui.Dialog().ok(addonname, startcastmsg)
except IOError:
    xbmcgui.Dialog().ok(addonname, "File not accessable...")
finally:
    f.close()


