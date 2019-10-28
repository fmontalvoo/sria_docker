from django.urls import path
from .views import inicio, detalle_noticia, detalle_evento, Noticias, Doctores, Nosotros,\
    Estatuto, Expresidentes, Miembros, Actividades

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ultimas_noticias/', Noticias.as_view(), name='noticias'),
    path('noticia/<int:id>', detalle_noticia, name='noticia'),
    path('actividad/<int:id>', detalle_evento, name='actividad'),
    path('nuestra_sociedad/', Nosotros.as_view(), name='nosotros'),
    path('directorio/', Doctores.as_view(), name='directiva'),
    path('estatutos/', Estatuto.as_view(), name='estatuto'),
    path('expresidentes/', Expresidentes.as_view(), name='expresidentes'),
    path('miembros/', Miembros.as_view(), name='miembros'),
    path('actividades_cientificas/', Actividades.as_view(), name='actividades'),
]
