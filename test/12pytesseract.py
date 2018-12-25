import  subprocess


p=subprocess.Popen([r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
                    r"C:\Users\Administrator\Desktop\001.jpg",
                    "chinese",
                    "-l",
                    "chi_sim"
                    ],
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE) #调用命令行
p.wait()#等待命令执行成功
file=open("chinese.txt","r")
print (file.read())