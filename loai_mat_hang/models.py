from django.db import models

# LoaiMatHang Model
class LoaiMatHang(models.Model):
    MaLoaiMatHang = models.AutoField(primary_key=True)
    TenLoaiMatHang = models.CharField(max_length=200, null=False)
