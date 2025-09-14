from django.urls import path

from . import views

urlpatterns = [
    path('khuvuc/<int:makhuvuc>/khachhang/<int:pk>', views.KhachHangDetailView.as_view(), name="khachhang-detail"),
]