from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),]
