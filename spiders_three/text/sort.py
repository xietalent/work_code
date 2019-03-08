
res_ = "大白菜"
with open(r"E:\word_book.txt" ,'a' ,encoding='utf8') as fp:
    fp.write(res_)
    fp.write("\n")
    fp.close()