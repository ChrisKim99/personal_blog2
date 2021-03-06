from django.urls import path
from . import views
from .views import home_list_view, select_book_detail_view

urlpatterns = [
    # the first value will be the names of actions 
    path('track_of_mind', views.select_track_of_mind,  name="track_of_mind"),

    # <int:pk> creates a primary key
    path('book/<int:pk>', select_book_detail_view.as_view(), name="book"),
    path('data_structure', views.select_data_structure,  name="track_of_mind"),
    path('data_analytic', views.select_data_analytic,  name="track_of_mind"),
    path('', home_list_view.as_view(), name="home"),
]