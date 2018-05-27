#Created By Death_Dealer
import subprocess, os
from subprocess import Popen, PIPE
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import ctypes
from ctypes import wintypes
import time
############################################################################################
print('''
██╗  ██╗ █████╗ ██╗      ██████╗         ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗
██║  ██║██╔══██╗██║     ██╔═══██╗██╗    ██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝
███████║███████║██║     ██║   ██║╚═╝    ██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗
██╔══██║██╔══██║██║     ██║   ██║██╗    ██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝
██║  ██║██║  ██║███████╗╚██████╔╝╚═╝    ╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝         ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝

███████╗██████╗ ██╗     ██╗████████╗███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
██╔════╝██╔══██╗██║     ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
███████╗██████╔╝██║     ██║   ██║   ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
╚════██║██╔═══╝ ██║     ██║   ██║   ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
███████║██║     ███████╗██║   ██║   ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝

████████╗ ██████╗  ██████╗ ██╗         ██╗   ██╗ ██╗   ██████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║   ██║███║   ╚════██╗
   ██║   ██║   ██║██║   ██║██║         ██║   ██║╚██║    █████╔╝
   ██║   ██║   ██║██║   ██║██║         ╚██╗ ██╔╝ ██║   ██╔═══╝
   ██║   ╚██████╔╝╚██████╔╝███████╗     ╚████╔╝  ██║██╗███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝   ╚═╝╚═╝╚══════╝
                                                                                        ''')
print('Made by: Death_Dealer')
print('Made for Eldewrito 0.6 and up.')
############################################################################################
#ScreenResDetect
user32 = ctypes.windll.user32
screensizeW = user32.GetSystemMetrics(0)
screensizeH = user32.GetSystemMetrics(1)

#Screen Setup
root = Tk()
root.withdraw()

path = (r'HALO_SP.pref')
if os.path.exists(path):
    text_file = open(path, "r")
    read = (text_file.read())
    input_loc = read.find("Install_Dir: ")
    cp_num = read[input_loc+14:]
    cp_num = cp_num.rstrip('"')
    infile = cp_num
    print('Install Found. - '+(cp_num))
else:
    infile =  filedialog.askopenfilename(title = "Select eldorado.exe ..",
        filetypes = (("Executable","*.exe"),("all files","*.*")))
    text_file = open(path, "w")
    text_file.write('Install_Dir: '+'"'+(infile)+'"')
    text_file.close()

#make .BACK of .cfg for eldorito to revert to after exit
dir_path = os.path.dirname(os.path.realpath(infile))
cfg = (dir_path+"/dewrito_prefs.cfg")
text_file = open(cfg, "r")
read = (text_file.read())
back = (dir_path+"/dewrito_prefs.BACK")
with open(back, "w") as text_file:
        text_file.write(read)
        text_file.close
'''
#Gamepad Enabling
#Settings.Gamepad "1"
dir_path = os.path.dirname(os.path.realpath(infile))
cfg = (dir_path+"/dewrito_prefs.cfg")
text_file = open(cfg, "r")
read = (text_file.read())
input_loc = read.find("Settings.Gamepad ")
cp_num = read[input_loc+18:input_loc+18+1]
cfg_1 = (read[:input_loc+18])
cfg_2 = read[input_loc+18+1:]
cp_num_new = int(1)
with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close
'''
Player_Count = input("How many players? = ")

if Player_Count == ('2'):
    print("Horizontal or Vertical Split?")
    Split_Control = input("(H)=Horizontal (V)=Vertical = ")
    if Split_Control == ('H') or Split_Control == ('h'):
        Res_Pos_P1 = (' 0,'+' 0,'+' '+str(int(screensizeW))+','+' '+str(int(screensizeH/2)))
        Res_Pos_P2 = (' 0,'+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW))+','+' '+str(int(screensizeH/2)))
    if Split_Control == ('V') or Split_Control == ('v'):
        Res_Pos_P1 = (' 0,'+' 0,'+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH)))
        Res_Pos_P2 = (' '+str(int(screensizeW/2))+','+' 0,'+str(int(screensizeW/2))+','+' '+str(int(screensizeH)))

if Player_Count == ('3'):
    print('Wide Screen on top or bottom?')
    Wide_Control = input("(T)=Top (B)=Bottom = ")
    if Wide_Control == ('T') or Wide_Control == ('t'):
        Res_Pos_P1 = (' 0,'+' 0,'+' '+str(int(screensizeW))+','+' '+str(int(screensizeH/2)))
        Res_Pos_P2 = (' 0,'+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
        Res_Pos_P3 = (' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
    if Wide_Control == ('B') or Wide_Control == ('b'):
        Res_Pos_P1 = (' 0,'+' 0,'+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
        Res_Pos_P2 = (str(int(screensizeW/2))+','+' 0,'+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
        Res_Pos_P3 = (' 0,'+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW))+','+' '+str(int(screensizeH/2)))

if Player_Count == ('4'):
    Res_Pos_P1 = (' 0,'+' 0,'+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
    Res_Pos_P2 = (str(int(screensizeW/2))+','+' 0,'+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
    Res_Pos_P3 = (' 0,'+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))
    Res_Pos_P4 = (' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2))+','+' '+str(int(screensizeW/2))+','+' '+str(int(screensizeH/2)))


KB_Input = input('Use Keyboard? Y/N=')

if KB_Input == ('N') or KB_Input == ('n'):
    pass

if KB_Input == ('Y') or KB_Input == ('y'):
    for x in range(1,int(Player_Count)+1):
        print("["+str(x)+"] "+"Player "+str(x))
    KB_Player = input('Witch Player will have KB/Mouse?:')


############################################################################################
#Handler Interval
HandlerInterval = ('15000')#10 seconds

############################################################################################
#make taskbar movable in layers

startup = ('''
#NoTrayIcon

WinSet, alwaysontop, toggle, ahk_class Shell_TrayWnd

''')
with open("bin/AHK/startup.ahk", "w") as script_r:
        script_r.write(str(startup))
        script_r.close()
subprocess.call(["bin/AHK/AutoHotkeyU64.exe", "bin/AHK/startup.ahk"])
############################################################################################
#Port Change
#reset port to 0 if its not at 0
dir_path = os.path.dirname(os.path.realpath(infile))
cfg = (dir_path+"/dewrito_prefs.cfg")
text_file = open(cfg, "r")
read = (text_file.read())
input_loc = read.find("Input.ControllerPort")
cp_num = read[input_loc+22:input_loc+22+1]
cfg_1 = (read[:input_loc+22])
cfg_2 = read[input_loc+22+1:]
cp_num_new = int(0)
with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close

#Set this to 1 to enable gamepad support if its not already enabled.
#Could be set to 0 on an instance to enable keyboard use.
#Settings.Gamepad "1"
############################################################################################
#PLAYER 1
if Player_Count >= '2':
    #Player 1
    if KB_Input == ('Y') or KB_Input ==('y'):
        if KB_Player == ('1'):
            dir_path = os.path.dirname(os.path.realpath(infile))
            cfg = (dir_path+"/dewrito_prefs.cfg")
            text_file = open(cfg, "r")
            read = (text_file.read())
            input_loc = read.find("Settings.Gamepad ")
            cp_num = read[input_loc+18:input_loc+18+1]
            cfg_1 = (read[:input_loc+18])
            cfg_2 = read[input_loc+18+1:]
            cp_num_new = int(0)
        with open(cfg, "w") as text_file:
                text_file.write(cfg_1+str(cp_num_new)+cfg_2)
                text_file.close
        if KB_Player != ('1'):
            #Gamepad Enabling
            #Settings.Gamepad "1"
            dir_path = os.path.dirname(os.path.realpath(infile))
            cfg = (dir_path+"/dewrito_prefs.cfg")
            text_file = open(cfg, "r")
            read = (text_file.read())
            input_loc = read.find("Settings.Gamepad ")
            cp_num = read[input_loc+18:input_loc+18+1]
            cfg_1 = (read[:input_loc+18])
            cfg_2 = read[input_loc+18+1:]
            cp_num_new = int(1)
            with open(cfg, "w") as text_file:
                text_file.write(cfg_1+str(cp_num_new)+cfg_2)
                text_file.close
    script_P1 = ("""
    ;P1
    #NoTrayIcon

    Run, """+(infile)+"""

    Sleep, """+(HandlerInterval)+"""

    WinGetTitle, Title, A

    oldTitle = %Title%
    NewTitle = %Title% P1

    WinSetTitle, %oldTitle%,,%NewTitle%

    WinActivate, %NewTitle%

    WinMove, %NewTitle%, ,"""+Res_Pos_P1+"""

    WinSet, Style, -0xC00000, %NewTitle%

    WinSet, Top
    Winset, Bottom,, ahk_class Shell_TrayWnd
    ;Sleep, 10
    ;WinSet, AlwaysOnTop, on, %NewTitle%
    """)


    with open("bin/AHK/tempP1.ahk", "w") as script_r:
        script_r.write(str(script_P1))
        script_r.close()

    subprocess.call(["bin/AHK/AutoHotkeyU64.exe", "bin/AHK/tempP1.ahk"])

    os.remove("bin/AHK/tempP1.ahk")
############################################################################################
#PLAYER 2
if Player_Count >= '2':
    #Player 2
    if KB_Input == ('Y') or KB_Input ==('y'):
        if KB_Player == ('2'):
            dir_path = os.path.dirname(os.path.realpath(infile))
            cfg = (dir_path+"/dewrito_prefs.cfg")
            text_file = open(cfg, "r")
            read = (text_file.read())
            input_loc = read.find("Settings.Gamepad ")
            cp_num = read[input_loc+18:input_loc+18+1]
            cfg_1 = (read[:input_loc+18])
            cfg_2 = read[input_loc+18+1:]
            cp_num_new = int(0)
        with open(cfg, "w") as text_file:
                text_file.write(cfg_1+str(cp_num_new)+cfg_2)
                text_file.close
        if KB_Player != ('2'):
            #Gamepad Enabling
            #Settings.Gamepad "1"
            dir_path = os.path.dirname(os.path.realpath(infile))
            cfg = (dir_path+"/dewrito_prefs.cfg")
            text_file = open(cfg, "r")
            read = (text_file.read())
            input_loc = read.find("Settings.Gamepad ")
            cp_num = read[input_loc+18:input_loc+18+1]
            cfg_1 = (read[:input_loc+18])
            cfg_2 = read[input_loc+18+1:]
            cp_num_new = int(1)
            with open(cfg, "w") as text_file:
                text_file.write(cfg_1+str(cp_num_new)+cfg_2)
                text_file.close
    #Edit CFG to change controller port
    dir_path = os.path.dirname(os.path.realpath(infile))
    cfg = (dir_path+"/dewrito_prefs.cfg")
    text_file = open(cfg, "r")
    read = (text_file.read())
    input_loc = read.find("Input.ControllerPort")
    cp_num = read[input_loc+22:input_loc+22+1]
    cfg_1 = (read[:input_loc+22])
    cfg_2 = read[input_loc+22+1:]
    cp_num_new = int(cp_num)+int(1)
    with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close

    #Settings.MusicVolume "100"
    #Running it on instances 2 will fix for all other instances
    dir_path = os.path.dirname(os.path.realpath(infile))
    cfg = (dir_path+"/dewrito_prefs.cfg")
    text_file = open(cfg, "r")
    read = (text_file.read())
    input_loc = read.find("Settings.MusicVolume ")
    cp_num = read[input_loc+22:input_loc+22+1]
    cfg_1 = (read[:input_loc+22])
    cfg_2 = read[input_loc+22+3:]
    cp_num_new = int(0)
    with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close

    script_P2 = ("""
    ;P2
    #NoTrayIcon

    Run, """+(infile)+"""

    Sleep, """+(HandlerInterval)+"""

    WinGetTitle, Title, A

    oldTitle = %Title%
    NewTitle = %Title% P2

    WinSetTitle, %oldTitle%,,%NewTitle%

    WinActivate, %NewTitle%

    WinMove, %NewTitle%, ,"""+Res_Pos_P2+"""

    WinSet, Style, -0xC00000, %NewTitle%
    WinSet, Top
    Winset, Bottom,, ahk_class Shell_TrayWnd
    """)

    with open("bin/AHK/tempP2.ahk", "w") as script_r:
        script_r.write(str(script_P2))
        script_r.close()

    subprocess.call(["bin/AHK/AutoHotkeyU64.exe", "bin/AHK/tempP2.ahk"])

    os.remove("bin/AHK/tempP2.ahk")
############################################################################################
#PLAYER 3
if Player_Count >= '3':
    #Player 3

    #Edit CFG to change controller port
    dir_path = os.path.dirname(os.path.realpath(infile))
    cfg = (dir_path+"/dewrito_prefs.cfg")
    text_file = open(cfg, "r")
    read = (text_file.read())
    input_loc = read.find("Input.ControllerPort")
    cp_num = read[input_loc+22:input_loc+22+1]
    cfg_1 = (read[:input_loc+22])
    cfg_2 = read[input_loc+22+1:]
    cp_num_new = int(cp_num)+int(1)
    with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close

    script_P3 = ("""
    ;P3
    #NoTrayIcon

    Run, """+(infile)+"""

    Sleep, """+(HandlerInterval)+"""

    WinGetTitle, Title, A

    oldTitle = %Title%
    NewTitle = %Title% P3

    WinSetTitle, %oldTitle%,,%NewTitle%

    WinActivate, %NewTitle%

    WinMove, %NewTitle%, ,"""+Res_Pos_P3+"""

    WinSet, Style, -0xC00000, %NewTitle%
    WinSet, Top
    Winset, Bottom,, ahk_class Shell_TrayWnd
    """)

    with open("bin/AHK/tempP3.ahk", "w") as script_r:
        script_r.write(str(script_P3))
        script_r.close()

    subprocess.call(["bin/AHK/AutoHotkeyU64.exe", "bin/AHK/tempP3.ahk"])

    os.remove("bin/AHK/tempP3.ahk")
############################################################################################
#PLAYER 4
if Player_Count == '4':
    #Player 4

    #Edit CFG to change controller port
    dir_path = os.path.dirname(os.path.realpath(infile))
    cfg = (dir_path+"/dewrito_prefs.cfg")
    text_file = open(cfg, "r")
    read = (text_file.read())
    input_loc = read.find("Input.ControllerPort")
    cp_num = read[input_loc+22:input_loc+22+1]
    cfg_1 = (read[:input_loc+22])
    cfg_2 = read[input_loc+22+1:]
    cp_num_new = int(cp_num)+int(1)
    with open(cfg, "w") as text_file:
        text_file.write(cfg_1+str(cp_num_new)+cfg_2)
        text_file.close

    script_P4 = ("""
    ;P4
    #NoTrayIcon

    Run, """+(infile)+"""

    Sleep, """+(HandlerInterval)+"""

    WinGetTitle, Title, A

    oldTitle = %Title%
    NewTitle = %Title% P4

    WinSetTitle, %oldTitle%,,%NewTitle%

    WinActivate, %NewTitle%

    WinMove, %NewTitle%, ,"""+Res_Pos_P4+"""

    WinSet, Style, -0xC00000, %NewTitle%
    WinSet, Top
    Winset, Bottom,, ahk_class Shell_TrayWnd
    """)

    with open("bin/AHK/tempP4.ahk", "w") as script_r:
        script_r.write(str(script_P4))
        script_r.close()

    subprocess.call(["bin/AHK/AutoHotkeyU64.exe", "bin/AHK/tempP4.ahk"])

    os.remove("bin/AHK/tempP4.ahk")

############################################################################################
#input('Press any key to Exit.')
#delete cfg for instal dir and rename .BACK to .cfg
text_file.close
time.sleep(3)
os.remove(dir_path+"/dewrito_prefs.cfg")

#restore info from .back to .cfg
dir_path = os.path.dirname(os.path.realpath(infile))
cfg = (dir_path+"/dewrito_prefs.BACK")
text_file = open(cfg, "r")
read = (text_file.read())
back = (dir_path+"/dewrito_prefs.cfg")
with open(back, "w") as text_file:
        text_file.write(read)
        text_file.close
input('Press any key to Exit.')
############################################################################################
