from django.urls import path
from . import views


urlpatterns = [
    # the first value will be the names of actions
    path('', views.index, name="index"),
    path('track_of_mind', views.select_track_of_mind,  name="track_of_mind"),
    path('book', views.select_book,  name="track_of_mind"),
    path('data_structure', views.select_data_structure,  name="track_of_mind"),
    path('data_analytic', views.select_data_analytic,  name="track_of_mind"),
]