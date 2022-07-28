from django.urls import path, include
from . import views

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'rsid', views.rsidViewSet)

urlpatterns = [
    path("rsid", views.RsidListView.as_view(), name="rsid.list"),
    path("rsid/<int:pk>", views.RsidDetailView.as_view(), name="rsid.detail"),
    path("rsid/<int:pk>/edit", views.RsidUpdateView.as_view(), name="rsid.update"),
    path("rsid/<int:pk>/delete", views.RsidDeleteView.as_view(), name="rsid.delete"),
    path("rsid/new", views.RsidCreateView.as_view(), name="rsid.new"),
    path("api/v1/rsid", views.RsidApiList.as_view(), name="api"),
]
