from django.contrib import admin
from django.urls import path, include
from . import views


handler404 = 'oc_lettings_site.views.custom_404'
handler404 = 'oc_lettings_site.views.custom_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('404/', views.custom_404, name='404'),
    path('500/', views.custom_500, name='500'),
    path('admin/', admin.site.urls),
]
