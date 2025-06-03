from django.urls import path
from . import views

urlpatterns = [
    path('nueva/', views.registrar_empresa, name='registrar_empresa'),
    path('lista/', views.lista_empresas, name='lista_empresas'),
    path('eliminar/<int:empresa_id>/', views.eliminar_empresa, name='eliminar_empresa'),
    path('editar/<int:empresa_id>/', views.editar_empresa, name='editar_empresa'),
    path('seleccionar-empresa/<int:empresa_id>/', views.seleccionar_empresa, name='seleccionar_empresa')



]
