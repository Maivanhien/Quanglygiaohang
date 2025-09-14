from django.db import models
from khu_vuc.models import KhuVuc

# KhachHang Model
class KhachHang(models.Model):
    MaKhachHang = models.AutoField(primary_key=True)
    MaKhuVuc = models.ForeignKey(KhuVuc, on_delete=models.SET_NULL, null=True)
    TenKhachHang = models.CharField(max_length=200, null=False)
    TenCuaHang = models.CharField(max_length=200, null=False)
    SoDTKhachHang = models.CharField(max_length=11, null=False)
    DiaChiEmail = models.CharField(max_length=200, null=True)
    DiaChiNhanHang = models.CharField(max_length=200, null=False)
