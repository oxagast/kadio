import xbmcaddon
import xbmcgui
import subprocess
import sys
import xbmc
import time
import os.path
from os import path
audiof = "/tmp/radio.mp3"
if path.exists('/usr/bin/rtl_fm') == False:
    xbmcgui.Dialog().ok(addonname, "Installing...")
    subprocess.call("yes | sudo apt install rtl-sdr lame", shell=True)
    subprocess.call("sudo wget https://raw.githubusercontent.com/osmocom/rtl-sdr/master/rtl-sdr.rules -O /lib/udev/rules.d/70-rtl-sdr.rules", shell=True)
    subprocess.call("sudo usermod -a -G plugdev osmc", shell=True)
    xbmcgui.Dialog().ok(addonname, "Please reboot osmc/kodi to finish installation.")
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
startcastmsg = "Tuning to configured FM frequency "
station = xbmcgui.Dialog().input("FM Base Station Number", type=xbmcgui.INPUT_NUMERIC)
decimal = xbmcgui.Dialog().input("FM Decimal Station", type=xbmcgui.INPUT_NUMERIC)
startcastmsg = startcastmsg + station + "." + decimal
#cmd = "sudo rtl_fm -g 50 -f " + station + "." + decimal + "M -M wfm -s 180k -E deemp | sox -t raw -r 16k -e signed -b 16 -c 1  - " + audiof + " &"
subprocess.call("sudo pkill -9 rtl_fm; sudo pkill -9 lame; sudo rm -f " + audiof, shell=True)
### bin/armhf/rtl_fm -f 103.3M -g 50 -M fm -s 200k -A std -l 0 -E deemp -r 75k | bin/armhf/lame -r -s 75 -V 5 --lowpass 15 --resample 44.1 -m m -b 64 - audio.mp3
#cmd = "sudo rtl_fm -f " + station + "." + decimal + "M -g 50 -M fm -s 200k -A std -l 0 -E deemp -r 75k | lame -r -s 75 -V 5 --lowpass 15 --resample 44.1 -m m -b 64 - " + audiof + " &"
cmd = "rtl_fm -f " + station + "." + decimal + "M -g 50 -M fm -s 200k -A std -l 0 -E deemp -r 75k | lame -r -s 75 -V 5 --lowpass 15 --resample 44.1 -m m -b 64 - " + audiof + " &"
subprocess.call(cmd, shell=True)
time.sleep(4)
try:
    f = open(audiof)
    xbmc.Player().play(audiof)
    xbmcgui.Dialog().ok(addonname, startcastmsg)
except IOError:
    xbmcgui.Dialog().ok(addonname, "File not accessable...")
finally:
    f.close()
