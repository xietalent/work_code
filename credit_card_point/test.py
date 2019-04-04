
import os

path = "images.exx"
a,b = os.path.splitext(path)
print(a)
print(b)
print(os.listdir(r".\images"))
ss = os.listdir(r".\images")
for s in ss:
    a, b = os.path.splitext(s)
    print(b)