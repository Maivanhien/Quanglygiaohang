from django.urls import path

from . import views

urlpatterns = [
    path('line-area-contracted-business', views.contracted_biz_view, name="contracted_biz_view"),
]