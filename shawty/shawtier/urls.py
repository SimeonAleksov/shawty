from django.urls import path
from .views import root

urlpatterns = [
    path('<str:url_hash>/', root, name='root')
]
