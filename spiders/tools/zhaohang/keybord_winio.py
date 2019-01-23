from ctypes import windll


import rabird.winio
import time
import atexit



# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

__winio = None

def __get_winio():
    global __winio

    if __winio is None:
            __winio = rabird.winio.WinIO()
            def __clear_winio():
                    global __winio
                    __winio = None
            atexit.register(__clear_winio)

    return __winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''
    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    # time.sleep(1)
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte( KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80)

def key_press(scancode, press_time = 0.2):
    key_down( scancode )
    time.sleep( press_time )
    key_up( scancode )

def shift_key_press(scancode,press_time = 0.2):
    key_down(0x2A)
    time.sleep(press_time)
    key_down(scancode)
    time.sleep(press_time)
    key_up(scancode)
    time.sleep(press_time)
    key_up(0x2A)

# Press 'A' key
# Scancodes references : https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
key_press(0x1E)

WIO_CODE = {
  'backspace': 0x0E, 'tab': 0x0F, 'enter': 0x1C, 'caps_lock': 0x3A, 'esc': 0x01,
  'spacebar': 0x39, '0': 0x0B, '1': 0x02, '2': 0x03,  '3': 0x04, '4': 0x05,
  '5': 0x06, '6': 0x07, '7': 0x08, '8': 0x09, '9': 0x0A, 'a': 0x1E, 'b': 0x30,
  'c': 0x2E, 'd': 0x20, 'e': 0x12, 'f': 0x21, 'g': 0x22, 'h': 0x23, 'i': 0x17,
  'j': 0x24, 'k': 0x25, 'l': 0x26, 'm': 0x32, 'n': 0x31, 'o': 0x18, 'p': 0x19,
  'q': 0x10, 'r': 0x13, 's': 0x1F, 't': 0x14, 'u': 0x16, 'v': 0x2F, 'w': 0x11,
  'x': 0x2D, 'y': 0x15, 'z': 0x2C, 'F1': 0x3B, 'F2': 0x3C, 'F3': 0x3D,
  'F4': 0x3E,'F5': 0x3F, 'F6': 0x40, 'F7': 0x41, 'F8': 0x42, 'F9': 0x43,
  'F10': 0x44, 'F11': 0x57, 'F12': 0x58, 'num_lock': 0x45, 'scroll_lock': 0x46,
  'left_shift': 0x2A, 'right_shift ': 0x36,'left_control': 0x1D, ',': 0x33,
  '-': 0x0C,'.': 0x34, '/': 0x35, '`': 0x29, ';': 0x27,  '[': 0x1A,']': 0x1B,
}

shift_code = {
    '~':0x29,'!': 0x02,'@':0x03, '#': 0x04, '$': 0x05,
  '%': 0x06, '^': 0x07, '&': 0x08, '*': 0x09, '(': 0x0A,')':0x0B, '_': 0x0C,'{': 0x1A,'}':0x1B,
}

u32 = windll.LoadLibrary('user32.dll')
print(u32)

# for i in "qweqwr123":
#     # print(i)
#     key_press(WIO_CODE['{}'.format(i)])
#     print(WIO_CODE['{}'.format(i)])



#输入
def input_key(element):
    upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    upper2 = '!@#$%^&*()_{}'
    # key_press(WIO_CODE['left_shift'])
    if element in upper:
        # print("测试开始")
        key_press(WIO_CODE['caps_lock'])
        time.sleep(0.1)
        key_press(WIO_CODE[element.lower()])
        time.sleep(0.1)
        key_press(WIO_CODE['caps_lock'])
        print("大写字母{}测试成功".format(element))
    elif element in upper2:
        shift_key_press(shift_code[element])
        print("shift+{}".format(element))
    else:
        if element not in WIO_CODE:
            print('error input char')
            return False
        key_press(WIO_CODE[element])
        time.sleep(0.1)
        print('非大写字母{}测试成功'.format(element))
    return True


def start_input(strs):
    for i in strs:
        input_key('{}'.format(i))


winio_list = 'My problem with these and many answers is that they approach it from an abstract, theoretical perspective, rather than starting with explaining simply why closures are necessary in Javascript and the practical situations in which you use them. You end up with a tl;dr article that you have to slog through, all the time thinking, "but, why?". I would simply start with: closures are a neat way of dealing with the following two realities of JavaScript: a. scope is at the function level, not the block level and, b. much of what you do in practice in JavaScript is asynchronous/event driven. –at'

start_input(winio_list)