from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^tb_coordenadas', views.CoordenadasList.as_view(), name='banco'),
    path('coordenadasUpdate', views.coordenadasUpdate, name="coordenadas_update"),
    url(r'^geojson', views.gerar, name='geojson'),
    url(r'^transmitir', views.transmitir, name='transmitir'),
    url(r'^motorista', views.motorista, name='motorista'),
    url(r'^rota', views.rota, name='rota'),
    url(r'^paradas', views.paradas, name='paradas'),
    url(r'^cadastro', views.cadastro, name='cadastro'),
    url(r'^cadastrar', views.cadastrar, name='cadastrar'),
    url(r'^newOnibus', views.criarOnibus, name="onibus_create"),
    url(r'^tb_paradas', views.ParadasView.as_view(), name="paradas_list"),
    url(r'^tb_rotas', views.RotasView.as_view(), name='rotas_list'),
    url(r'^tb_bus', views.OnibusView.as_view(), name='lista de Rotas'),
    url(r'^tb_distanciasR', views.DistanciasRView.as_view(), name='lista de distancia das Rotas'),
    url(r'^tb_distanciaTR', views.DistanciaTRView.as_view(), name='lista de distancia percorrida bus tempo real'),
    url(r'^deleteRotas', views.deleteRotas, name='Delete rota'),
    path('editarParada/<int:id>', views.editarParada, name='parada_editar'),
    url(r'^editarOnibus', views.editarOnibus, name='editar onibus'),
    url(r'^verRota', views.verRota, name='rota_geojson'),
]
