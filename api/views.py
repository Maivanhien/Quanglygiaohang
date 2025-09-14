from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from khach_hang.models import KhachHang
from .serializers import KhachHangSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class WalletAPIView(generics.DestroyAPIView):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer
