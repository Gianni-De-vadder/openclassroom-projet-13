from django.urls import path
from lettings import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),  # Mettez 'index' ici au lieu de 'letting'
    path('<int:letting_id>/', views.letting, name='letting'),
]
