from mans import  Mans
from gun import Gun
from clip import Clip

clip = Clip()
clip.set_nums(30)

gun = Gun(clip)

mans = Mans(gun)

# for i in range(1,300):
# i = 1
while True:
    mans.shoot()
