from django.contrib import admin
from django.urls import path
#   from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.movie_list_view, name='movies'),
    path('<int:pk>/', views.movie_detail_view, name='movie'),
    path('movie_create/', views.movie_create_view, name='movie_create'),
    path('movie_update/<int:pk>/', views.movie_update_view, name='movie_update'),
    path('movie_delete/', views.movie_delete_view, name='movie_delete'),
    path('movie_scraping', views.run_webscraping_view, name='movie_scraping'),
]
