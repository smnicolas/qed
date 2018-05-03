from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materias', views.MateriasView.as_view(), name='materias'),
    path('<materia>', views.CuatrimestreView.as_view(), name='materia'),
    path('<materia>/<cuatrimestre>/practica<int:practica>/<int:numero>', views.enunciado, name='enunciado')
]
