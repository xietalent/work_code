from django.db import models

# Create your models here.


class User(models.Model):
    # id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    passwd = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        app_label='datasapp'
        db_table ='user'

class Card_score(models.Model):
    #积分和消费记录
    score = models.CharField(max_length=100)
    record = models.CharField(max_length=1000)

    # print("积分"+str(score))
    print(record)
    class Meta:
        app_label='datasapp'
        db_table ='card_score'
