from django.db import models
from don_hang_giao_hang.models import DonHangGiaoHang
from loai_mat_hang.models import LoaiMatHang

# ChiTietDonHang Model
class ChiTietDonHang(models.Model):
    MaChiTietDonHang = models.AutoField(primary_key=True)
    MaDonHangGiaoHang = models.ForeignKey(DonHangGiaoHang, on_delete=models.CASCADE, unique=True)
    TenSanPhamDuocGiao = models.CharField(max_length=200, null=False, unique=True)
    SoLuong = models.IntegerField(default=0)
    TrongLuong = models.FloatField(default=0)
    MaLoaiMatHang = models.ForeignKey(LoaiMatHang, on_delete=models.SET_NULL, null=True)
    TenThuHo = models.CharField(max_length=200, null=False)
