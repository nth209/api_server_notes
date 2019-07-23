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
    device = models.CharField("Thiết bị đăng nhập khi lưu", max_length=255, default="")
    detele_flg = models.IntegerField(default=0)


# == == = == == == == == == == == == == Path Models == == == == == == == == == == == == == == = #

class linkTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name link", max_length=255, default="Unknown")
    path = models.TextField("Path Url", default="")
    des = models.CharField("Mô tả", default="",max_length=255)
    device = models.CharField("Thiết bị đăng nhập khi lưu",max_length=255, default="")
    user_id = models.IntegerField(default=None)
    display_flg = models.IntegerField(default=2) # 0 chi nguoi do moi co the xem # 1 moi nguoi duoc xem 2 chi nguoi do va admin duoc xem
    delete_flg = models.IntegerField(default=0)

# == == = == == == == == == == == == == Notes Models == == == == == == == == == == == == == == = #