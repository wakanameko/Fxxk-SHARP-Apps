# coding: UTF-8
import tkinter as tk
import webbrowser
import platform
import os
from tkinter import messagebox
import subprocess

#########
# SETUP
#########
if not os.name == 'nt':messagebox.showinfo('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

APPNAME = "FxxkSHARPApps"
VERSION = "2.2"
DEVELOPER = "wakanameko2"

APPSID = [
    '''jp.co.sharp.android.settingsaquosusefull''',
    '''jp.co.sharp.android.scshocapture2''',
    '''sharp.jp.android.makersiteappli''',
    '''jp.co.sharp.android.iwnnime.ml''',
    '''jp.co.sharp.android.shframecapture''',
    '''jp.co.sharp.android.karadamate''',
    '''jp.co.sharp.android.pseudlock.helper''',
    '''jp.co.sharp.android.emopar''',
    '''jp.co.sharp.android.emopar.internalcontent''',
    '''jp.co.sharp.android.emopar.internalcontent2''',
    '''jp.co.sharp.android.sharpdatabackup''',
    '''jp.co.sharp.android.scrollauto''',
    '''jp.co.sharp.android.shrobodockservice''',
    '''jp.co.sharp.android.SHWirelessOutput''',
    '''jp.co.sharp.android.shinstructionmanual02mb''',
    '''jp.co.sharp.android.shinstructionmanual02mc''',
    '''jp.co.sharp.android.LockWeatherWidget''',
    '''jp.co.sharp.android.startuptutorial_ps''',
    '''jp.co.sharp.android.friendlink''',
    '''jp.co.sharp.android.service.hikarieffect''',
    '''jp.co.sharp.android.shlivewallpaper''',
    '''jp.co.sharp.android.emopa.overlayservice''',
    '''jp.co.sharp.android.emopa.systemservice''',
    '''jp.co.sharp.android.wallpaper3d''',
    '''jp.co.sharp.android.lockwallpaperchanger''',
    '''com.mobisystems.office''',
    '''jp.co.sharp.android.antitok''',
    '''jp.co.sharp.android.pseudolock.helper''',
    '''jp.co.sharp.android.kittingservice''',
    '''jp.co.sharp.android.kittingsuw''',
    '''jp.co.sharp.android.kittingapp''',
    '''jp.co.sharp.android.usbchargingalart''',
]
APPSID_SAIFU = [
    '''jp.co.sharp.android.nfcsettings''',
]

print(len(APPSID), len(APPSID_SAIFU))
print(APPNAME + " ver." + str(VERSION))
print('Developer' + DEVELOPER)

ur = platform.uname()
print(ur.system + '\n' + ur.release + '\n' + ur.version + '\n' + ur.processor)

if (ur.release == 'xp') or (ur.release == '2000') or (ur.release == 'me') or (ur.release == '98') or (ur.release == '95'):messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

#########
# setup main window
#########
baseGround = tk.Tk()

if (ur.release == 'vista') or (ur.release == '7') or (ur.release == '8') or (ur.release == '8.1') or (ur.release == '2012ServerR2'):
    baseGround.geometry('600x75')
    print('built a window for windows VISTA ~ 2012ServerR2')
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':baseGround.geometry('575x70')
    #Windows10
    else:baseGround.geometry('525x60')

baseGround.title(APPNAME + " | " + "ver" + VERSION + " | by " + DEVELOPER)

baseGround.resizable(width = False, height = False)

data = '''R0lGODlhAAEAAffgAAAAADY2Njk5OTc3ODAwLjExVldXV15dXFhYV0RERFxbYlpa
        a1ZVa01NdVJRelVVclFPeV9gYGJjZGJnaGRqbG1tbWVucWh2emh1eXd3d3p6eml9
        Z2BfY3WMXouqNJO0M5q9NZe4No2tL4KePJ7CNp/DOKTJNqHGOqXKOajLP6DFN4Kc
        UKzOSanMQ7PSV6zLVLrXaL/Zc8Hbdy8wlykppCoqqignoDs7qS0ttS8vuzw8szk5
        vTQ0uk5OhUtLjEdHllJdm1Zhn1lml1hlh2t/hGZ4g319lUNEp1JcpEBFsl5lpS8v
        yzIyxTMzzDw8zjk5xjAvzkA/z0FBz0tLzFdXykRE0EtL0khH0VRU1Fxc1lhX1VBP
        02Zny2Fh12Rk2Ghn2Wxs2nNz3Hx83nh32XNzzz1BuYB/322DiW2CiHKOlnKPmXST
        m3OQl3ibpnuAt3qirX2qtn2ptXC+2G+92HTC3HjF33nG4HzK5IWFhYyMjJ2dnZOT
        k4WQloCwvaampq2trbW1tb2+vbe4t66us5ihnb3Gpsfeg8nfiMXUmc/jldHkmtDj
        l8vhjdnprNbmpdzqteLuvsfPsIGB34+PzYK0xIS7y4e/0bm507Cwy4SE4IyM4oiH
        4ZSU5Jub5piX5aGh56Wl6Kur6qin6bS07Ly87rCv66Cf58C/74vK3YjE1YfBz4HP
        6YfO5ITT7IzU647R5ZLb75DW7IjX8I3b9IfW8JLc85Hf+Jbl/5jo/5Xi+cHBwcfH
        y8nJ1dTV1Nzd3NXV2dHRz+Tuw+fxy+fxyuDg3+/23Ov00/D238HA78XE8MzM8sjH
        8dTT9Nzc9tjX9ePj4unp6ezs7Orq6uXm6O/w7fX56ODg9+Xl+evr+vDw8PHx8fPz
        8/Ly8vHx8fT0/P39/f////3+/f////n69t7g4gAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAAAQABAAj/AAEIHEiwoMGDCBMqXMiw
        ocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2b
        BwXoHKCzp8+fQIMKHUqUKM6jSB/qDBCgqNOnUKEyFZC0qlWCSw3k+QOoq9evYMOK
        HUu2rFg/GhI0vcr2aE8Nv7jJnUu3rt27ePPq1RtNkIG1bQPPFBCgwrO62epGi7ZX
        MePGdxdze/wYryC1VAVrdqlTUGPJkOcmDi16crRslflqALy5NUrCBnzJHY2X8jNp
        dLNJ2827t+/fuLllSzw8deM/Ol0rN0n4wGHhjafp0bBHNrdpfvBo3869u/c8ukyT
        /64LKPny8yGbPy+O2rhcXRLi/3kfv779+/jr45k2mbZd0HKBVl5m6BXIkXqzmbaY
        e7pUIN97DuYnIX77TUZXZe0B2B43AxrooUYInjaXe4xhR91z0vyRx4ostujii3vs
        UlqAJCa2oFwdfqhjRSFe6N+N0Uzz2GjR8LZgkdIsttuRR454YWoA3siheTtWCVGP
        e7mn2F7+OXahl3flaOWYDIUI4F1d/keacU32l5uWUxJI5pw5BeDceCOe+RlfeM4l
        Jp2ADoRgmn3ONU6hiMYZ6KICIciNL37oIemklFZq6aWYZqrppYA89iejczqqSwIV
        aJDBqaimquqqGWhgKquwpv/qqquxtmqABMF9CuqYohowzTfABivssMQWa+yxyA77
        B644Urkrmb1Kk+y01FaL7LK5OvusldFa6+2302LbrJzbVtktuOimC6y4ipbLq53P
        6XKAtOrW6y27urrroajzgltNNelWMw644m6Tr74FnustJDIM/G0xMAD8Lb7aImyg
        wtZWA0Mj4B5yCLoUk2txwvC+ZwC930ISsbfCuFAMyMy2C1INOOSQAxM456yzzjbj
        UMPIF2Fs7TgyKALsOMcE08giiSSiyCPDSPyNDIukG/JGNNSMcxNcd+3112B/jXMO
        PgOtVMnc6HJyusPAEIwjMbCQAgom1G0CCi24IMMjjaz/DLM0iR3skA04bB324Ygn
        3jXOONBgdkJCW2uMCy3QjcLlmGNeNwopxCD1xLgGXnFDhStu+ummM4HD4wVFPu04
        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
        IjfyI0fyJFfyJXepgAAAOw==
     '''
baseGround.tk.call('wm', 'iconphoto', baseGround._w, tk.PhotoImage(data=data))
    
#########
# core
#########
def running(option):
    label1 = tk.Label(baseGround, text='処理を実行中 (' + option + ')').place(x=290,y=15)
    if (option == "uninstall") or (option =="disable"):
        osaifuProtect = messagebox.askyesno('確認','おサイフケータイ機能を残しますか？')
    elif (option == "install") or (option == "enable"):
        for i in range(0, len(APPSID_SAIFU)):
            osaifuProtect = True
            if option == "install":
                subprocess.call('''adb shell cmd package install-existing ''' + APPSID_SAIFU[i])
            elif option == "enable":
                subprocess.call('''adb shell pm enable --user 0 ''' + APPSID_SAIFU[i])
    
    for i in range(0, len(APPSID)):
        if option == "uninstall":
            subprocess.call('''adb shell pm uninstall -k --user 0 ''' + APPSID[i])
        elif option == "install":
            subprocess.call('''adb shell cmd package install-existing ''' + APPSID[i])
        elif option == "disable":
            subprocess.call('''adb shell pm disable-user --user 0 ''' + APPSID[i])
        elif option == "enable":
            subprocess.call('''adb shell pm enable --user 0 ''' + APPSID[i])

    if osaifuProtect == False:
        for i in range(0, len(APPSID_SAIFU)):
            if option == "uninstall":
                subprocess.call('''adb shell pm uninstall -k --user 0 ''' + APPSID_SAIFU[i])
            elif option == "disable":
                subprocess.call('''adb shell pm disable-user --user 0 ''' + APPSID_SAIFU[i])
    else:
        pass

    print('All done')
    label1 = tk.Label(baseGround, text='All Done                           ').place(x=290,y=15)
    return True
    
def btn_click_adb():
    webbrowser.open('https://dl.google.com/android/repository/platform-tools_r33.0.1-darwin.zip')

#########
# Widgets
#########
if (ur.release == 'vista') or (ur.release == '7'):label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=253,y=48)
elif (ur.release ==  '8') or (ur.release == '8.1') or (ur.release == '2012ServserR2'):label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=290,y=48)
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=270,y=43)
    #Windows10
    else:label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)

if (ur.release == 'vista') or (ur.release == '7'):
    button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 530, y=41)
elif (ur.release == '8') or (ur.release == '8.1') or (ur.release == '2012ServserR2'):
    button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 525, y=43)
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 500, y=40)
    #Windows10
    else:button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)

button = tk.Button(
    baseGround, text='Uninstall', command = lambda:running("uninstall")).place(x= 10, y=10)
button2 = tk.Button(
    baseGround, text='Install', command = lambda:running("install")).place(x= 90, y=10)
button3 = tk.Button(
    baseGround, text='Disable', command = lambda:running("disable")).place(x= 155, y=10)
button4 = tk.Button(
    baseGround, text='Enable', command = lambda:running("enable")).place(x= 225, y=10)

baseGround.mainloop()
