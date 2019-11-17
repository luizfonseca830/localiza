from django.urls import path
from .views import *

urlpatterns = [
    path('list/', clientes_list, name='cliente_list'),
    path('new/', clientes_new, name='cliente_new'),
    path('update/<int:id>/', clientes_update, name='cliente_update'),
    path('delete/<int:id>/', clientes_delete, name='cliente_delete'),
]
