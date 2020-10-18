from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    #path('specialties/', views.specialties, name='specialties'),
    #path('menu/', views.mainmenu, name='mainmenu'),
]