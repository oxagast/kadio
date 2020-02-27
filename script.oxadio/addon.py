import xbmcaddon
import xbmcgui
import os
import sys

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
ssdialog = xbmcgui.Dialog()
ssret = ssdialog.yesno('Kodi', 'Do you want to start the radio?')
if ssret == True:
    startcastmsg = "Tuning to configured FM frequency "
    stopcastmsg = "Shutting down radio..."
    station = xbmcgui.Dialog().input("FM Base Station Number", type=xbmcgui.INPUT_NUMERIC)
    decimal = xbmcgui.Dialog().input("FM Decimal Station", type=xbmcgui.INPUT_NUMERIC)
    startcastmsg = startcastmsg + station + "." + decimal
    xbmcgui.Dialog().ok(addonname, startcastmsg)
    os.system("rtl_fm -g 50 -f " + station + "." + decimal + "M -M wfm -s 180k -E deemp | play -r 180k -t raw -e s -b 16 -c 1 -V1 - lowpass 16k")
else:
    os.system("pkill rtl_fm")
