import xbmcaddon
import xbmcgui
import subprocess
import sys
import xbmc
import time
audiof = '/home/osmc/.kodi/addons/script.kadio/radio.wav'
subprocess.call("pkill -9 rtl_fm; pkill -9 sox; rm -f " + audiof, shell=True)
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
startcastmsg = "Tuning to configured FM frequency "
stopcastmsg = "Shutting down radio..."
station = xbmcgui.Dialog().input("FM Base Station Number", type=xbmcgui.INPUT_NUMERIC)
decimal = xbmcgui.Dialog().input("FM Decimal Station", type=xbmcgui.INPUT_NUMERIC)
startcastmsg = startcastmsg + station + "." + decimal
cmd = "rtl_fm -g 50 -f " + station + "." + decimal + "M -M wfm -s 180k -E deemp | sox -t raw -r 16k -e signed -b 16 -c 1  - " + audiof + " &"
subprocess.call(cmd, shell=True)
time.sleep(2)
try:
    f = open(audiof)
    if xbmc.Player().isPlaying() == False:
        xbmc.Player().play(audiof)
        xbmcgui.Dialog().ok(addonname, startcastmsg)
    if xbmc.Player().isPlaying() == True:
        player.pause()
        xbmc.Player().play(audiof)
        xbmcgui.Dialog().ok(addonname, startcastmsg)
except IOError:
    xbmcgui.Dialog().ok(addonname, "File not accessable...")
finally:
    f.close()


