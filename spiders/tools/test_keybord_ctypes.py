import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def press_key(hexKeyCode, presstime=0.01):
    PressKey(hexKeyCode)
    time.sleep(presstime)
    ReleaseKey(hexKeyCode)


# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
WIO_CODE = {
    'backspace': 0x0E, 'tab': 0x0F, 'enter': 0x1C, 'caps_lock': 0x3A, 'esc': 0x01,
    'spacebar': 0x39, '0': 0x0B, '1': 0x02, '2': 0x03, '3': 0x04, '4': 0x05,
    '5': 0x06, '6': 0x07, '7': 0x08, '8': 0x09, '9': 0x0A, 'a': 0x1E, 'b': 0x30,
    'c': 0x2E, 'd': 0x20, 'e': 0x12, 'f': 0x21, 'g': 0x22, 'h': 0x23, 'i': 0x17,
    'j': 0x24, 'k': 0x25, 'l': 0x26, 'm': 0x32, 'n': 0x31, 'o': 0x18, 'p': 0x19,
    'q': 0x10, 'r': 0x13, 's': 0x1F, 't': 0x14, 'u': 0x16, 'v': 0x2F, 'w': 0x11,
    'x': 0x2D, 'y': 0x15, 'z': 0x2C, 'F1': 0x3B, 'F2': 0x3C, 'F3': 0x3D,
    'F4': 0x3E, 'F5': 0x3F, 'F6': 0x40, 'F7': 0x41, 'F8': 0x42, 'F9': 0x43,
    'F10': 0x44, 'F11': 0x57, 'F12': 0x58, 'num_lock': 0x45, 'scroll_lock': 0x46,
    'left_shift': 0x2A, 'right_shift ': 0x36, 'left_control': 0x1D, ',': 0x33,
    '-': 0x0C, '.': 0x34, '/': 0x35, '`': 0x29, ';': 0x27, '[': 0x1A, ']': 0x1B,
}

shift_code = {
    '~': 0x29, '!': 0x02, '@': 0x03, '#': 0x04, '$': 0x05,
    '%': 0x06, '^': 0x07, '&': 0x08, '*': 0x09, '(': 0x0A, ')': 0x0B, '_': 0x0C, '{': 0x1A, '}': 0x1B,':':0x27,
}

# while True:
#     while (True):
#         PressKey(0x11)
#         time.sleep(0.2)
#         ReleaseKey(0x11)
#         time.sleep(0.05)
#         PressKey(0x15)
#         time.sleep(0.05)
#         ReleaseKey(0x15)
#         time.sleep(0.05)
#         PressKey(0x1A)
#         time.sleep(0.05)
#         ReleaseKey(0x1A)
#
#         time.sleep(0.05)
#         PressKey(0x1C)
#         time.sleep(0.05)
#         ReleaseKey(0x1C)
#         time.sleep(0.05)
#         PressKey(0x1C)
#         time.sleep(0.05)
#         ReleaseKey(0x1C)
#         # time.sleep(0.05)
#         # PressKey(0x39)
#         # time.sleep(0.05)
#         # ReleaseKey(0x39)


def input_key(element):
    upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    upper2 = '!@#$%^&*()_{}'
    # key_press(WIO_CODE['left_shift'])
    if element in upper:
        # print("测试开始")
        press_key(WIO_CODE['caps_lock'])
        time.sleep(0.01)
        press_key(WIO_CODE[element.lower()])
        time.sleep(0.1)
        press_key(WIO_CODE['caps_lock'])
        print("大写字母{}测试成功".format(element))
    elif element in upper2:
        PressKey(WIO_CODE['left_shift'])
        time.sleep(0.01)
        press_key(shift_code[element])
        time.sleep(0.01)
        ReleaseKey(WIO_CODE['left_shift'])

        print("shift+{}".format(element))
    else:
        if element not in WIO_CODE:
            print('error input char')
            return False
        press_key(WIO_CODE[element])
        time.sleep(0.01)
        print('非大写字母{}测试成功'.format(element))
    return True
# datalist = input("请输入：")
datalist = 'My problem with these and many answers is that they approach it from an abstract, theoretical perspective, rather than starting with explaining simply why closures are necessary in Javascript and the practical situations in which you use them. You end up with a tl;dr article that you have to slog through, all the time thinking, "but, why?". I would simply start with: closures are a neat way of dealing with the following two realities of JavaScript: a. scope is at the function level, not the block level and, b. much of what you do in practice in JavaScript is asynchronous/event driven. –at '
time.sleep(2)
# datalist = "I am trying to build a table from my firebase database. However, in the last two columns, they show [object][object]. Those data were coming from the sensor reading. I only want to show the latest value reading by the sensor through in my table. here is my database structure in firebase():"

for _ in datalist:
    if _ is ' ':
        input_key('spacebar')
        print("空格")
    else:
        input_key('{}'.format(_))
