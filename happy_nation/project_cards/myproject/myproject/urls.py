from django.contrib import admin
from django.urls import include, path
from cartao.views import home  # Importe a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartao/', include('cartao.urls')),
    path('', home, name='home'),  # Adicione esta linha
]