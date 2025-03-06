from django.urls import path
from . import views

urlpatterns = [
path('index/', views.index, name='index'),
path('index/matematika.html/', views.mathematics, name='mathematics'),
path('index/sustezaniq.html', views.sustezaniq, name='sustezaniq'),
path('index/bel.html', views.bel, name='bel'),
path('index/kalendar.html', views.kalendar, name='kalendar'),
path('index/ang.html', views.ang, name='ang'),
path('index/himiq.html', views.himiq, name='himiq') ,
path('index/geo.html', views.geo, name='geo') ,
path('index/istoriq.html', views.istoriq, name='istoriq'),
path('index/bio.html', views.bio, name='bio'),
path('index/fizika.html', views.fizika, name='fizika'),
path('index/it.html', views.it, name='it'),
]