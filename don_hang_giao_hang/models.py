from django.db import models
from khach_hang.models import KhachHang
from thanh_vien_giao_hang.models import ThanhVienGiaoHang
from dich_vu.models import DichVu
from khu_vuc.models import KhuVuc
from khoang_thoi_gian.models import KhoangThoiGian

# DonHangGiaoHang Model
class DonHangGiaoHang(models.Model):
    MaDonHangGiaoHang = models.AutoField(primary_key=True)
    MaKhachhang = models.ForeignKey(KhachHang, on_delete=models.SET_NULL, null=True)
    MaThanhVienGiaoHang = models.ForeignKey(ThanhVienGiaoHang, on_delete=models.SET_NULL, null=True)
    MaDichVu = models.ForeignKey(DichVu, on_delete=models.SET_NULL, null=True)
    MaKhuVuc = models.ForeignKey(KhuVuc, on_delete=models.SET_NULL, null=True)
    TenNguoiNhan = models.CharField(max_length=200, null=False)
    DiaChiGiaoHang = models.CharField(max_length=200, null=False)
    SoDTNguoiNhan = models.CharField(max_length=11, null=False)
    MaKhoangThoiGian = models.ForeignKey(KhoangThoiGian, on_delete=models.SET_NULL, null=True)
    NgayGiaoHang = models.DateField()
    PhuongThucThanhToan = models.CharField(max_length=20, null=False)
    TrangThaiPheDuyet = models.CharField(max_length=200, null=True)
    TrangThaiGiaoHang = models.CharField(max_length=200, null=True)
