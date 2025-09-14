from rest_framework import serializers
from khach_hang.models import KhachHang

class KhachHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhachHang
        fields = '__all__'