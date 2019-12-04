from django.urls import path
from .views import *

urlpatterns = [
    path('list/', locacoes_list, name='locacoes_list'),
    path('new/', locacoes_new, name='locacoes_new'),
    path('update/<int:id>/', locacoes_update, name='locacoes_update'),
    path('delete/<int:id>/', locacoes_delete, name='locacoes_delete'),
]
