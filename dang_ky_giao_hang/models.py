from django.db import models
from thanh_vien_giao_hang.models import ThanhVienGiaoHang
from khoang_thoi_gian.models import KhoangThoiGian

# DangKyGiaoHang Model
class DangKyGiaoHang(models.Model):
    MaDangKyGiaoHang = models.AutoField(primary_key=True)
    MaThanhVienGiaoHang = models.ForeignKey(ThanhVienGiaoHang, on_delete=models.SET_NULL, null=True)
    MaKhoangThoiGian = models.ForeignKey(KhoangThoiGian, on_delete=models.SET_NULL, null=True)
