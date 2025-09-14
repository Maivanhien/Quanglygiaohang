from django.db import models

# DichVu Model
class DichVu(models.Model):
    MaDichVu = models.AutoField(primary_key=True)
    TenDichVu = models.CharField(max_length=200, null=False)
