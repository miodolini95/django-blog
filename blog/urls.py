from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('motoryzacja', views.motoryzacja, name='motoryzacja_category'),
    path('inne', views.inne, name='inne_category'),
    path('elektronika', views.elektronika, name='elektronika_category'),
    path('sport', views.sport, name='sport_category'),
    path('uslugi', views.uslugi, name='uslugi_category'),
]