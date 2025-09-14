from django.db import models

# ThanhVienGiaoHang Model
class ThanhVienGiaoHang(models.Model):
    MaThanhVienGiaoHang = models.AutoField(primary_key=True)
    TenThanhVienGiaoHang = models.CharField(max_length=200, null=False)
    NgaySinh = models.DateField()
    GioiTinh = models.CharField(max_length=3, null=False)
    SoDTThanhVien = models.CharField(max_length=11, null=False)
    DiaChiThanhVien = models.CharField(max_length=200, null=False)
