import pymysql
# from huaxia.SeleniumMiddleware import process_request

connet = pymysql.Connect(host="47.97.217.36",user = "root",password="root",database="stu",port = 3306,charset="utf8")

cursor = connet.cursor()

sql = "select version();"

cursor.execute(sql)

res = cursor.fetchone()
print(res)
print(type(res))
