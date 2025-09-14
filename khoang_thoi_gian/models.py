from django.db import models

# KhoangThoiGian Model
class KhoangThoiGian(models.Model): 
    MaKhoangThoiGian = models.AutoField(primary_key=True)
    MoTa = models.CharField(max_length=200, null=True)
