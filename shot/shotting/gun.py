from time import sleep

class Gun(object):
    def __init__(self,clip):
        self.clip = clip
        self.nums = 0

    def shoot(self):
        number =self.clip.get_nums()
        if number < 0:
            print("您已经没有子弹了,请更换弹夹")
        elif number == 0:
            self.clip.set_nums(number - 1)
            print("子弹打完了,请更换弹夹")
            # c_clip = input("子弹打完了是否更换弹夹:")
            # if c_clip =="是":
            self.clip.set_nums(30)
        elif number <= 30:
            self.nums +=1
            self.clip.set_nums(number - 1)
        sleep(0.1)
        print("您打了1发子弹,剩余{},一共射击{}发子弹".format (self.clip.get_nums(),self.nums))