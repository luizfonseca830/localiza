from django.urls import path
from .views import *

urlpatterns = [
    path('list/', automoveis_list, name='automovel_list'),
    path('new/', automoveis_new, name='automovel_new'),
    path('update/<int:id>/', automoveis_update, name='automovel_update'),
    path('delete/<int:id>/', automoveis_delete, name='automovel_delete'),
    path('listlocados/', automoveis_locados, name='automoveis_locados'),
]
