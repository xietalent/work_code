

class Clip(object):
    def __init__(self):
        self.__number = 0
    def get_nums(self):
        return self.__number

    def set_nums(self,num):
        if num <= 30 and num >= 0:
            self.__number = num
        else:
            print("憨憨,已经没子弹了,请装弹")
