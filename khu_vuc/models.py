from django.db import models

# KhuVuc Model
class KhuVuc(models.Model):
    MaKhuVuc = models.AutoField(primary_key=True)
    TenKhuVuc = models.CharField(max_length=200, null=False)
