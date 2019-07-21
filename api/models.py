######author Nguyen Thanh Hai######
from django.db import models
from django.contrib.auth.models import User


class thanhpho(models.Model):
    id_thanhpho = models.IntegerField(primary_key=True)
    ten_thanhpho = models.CharField("Tên thành phố",max_length=255)
    def __str__(self):
        return self.ten_thanhpho

class quan(models.Model):
    id_quan = models.IntegerField(primary_key=True)
    id_thanhpho = models.ForeignKey(thanhpho, on_delete=models.CASCADE)
    ten_quan = models.CharField("Tên Quận", max_length=255)
    def __str__(self):
        return self.ten_quan

class xa(models.Model):
    id_xa = models.IntegerField(primary_key=True)
    id_quan = models.ForeignKey(quan, on_delete=models.CASCADE)
    ten_xa = models.CharField("Tên xã", max_length=255)
    def __str__(self):
        return self.ten_xa


class userDetail(models.Model):
    id  = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    hinh_anh = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    id_thanhpho = models.ForeignKey(thanhpho, on_delete=models.CASCADE)
    id_quan = models.ForeignKey(quan, on_delete=models.CASCADE)
    id_xa = models.ForeignKey(xa, on_delete=models.CASCADE)
    detele_flg = models.IntegerField(default=0)