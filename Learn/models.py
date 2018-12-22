from django.db import models


# Create your models here.


# creat table showPic(  # SQL Manager 里面的SQL语言
#     name varchar(20),
#     size:int,
#     height:int,
#     width:int,
#     shooter:varchar(20),
#     mk_time:date,
#
# )

class PicLab(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    mk_time = models.DateField()


class Staff(models.Model):
    LoginID = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=20)
    Name = models.CharField(max_length=10)
    Sex = models.BooleanField(default=True)
    EmailAdd = models.CharField(max_length=30,default="")
    TelNum = models.CharField(max_length=20,default="")
    Birthday = models.DateField(max_length=20, null=True)
    JoinTime = models.DateField()
    LessonCover = models.IntegerField(default=0)


