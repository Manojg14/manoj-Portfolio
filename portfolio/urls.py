from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    path('', views.home_page, name='home'),
]


