from django.contrib import admin
from django.urls import path, include
from cartao.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartao/', include('cartao.urls')),
    path('', home, name='home'),
]