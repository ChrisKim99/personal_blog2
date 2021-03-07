from django.urls import path
from . import views
from .views import home_view, article_view, add_post_view, update_post_view, delete_post_view, add_category_view, category_view, category_list_view

urlpatterns = [
    
    path('', home_view.as_view(), name='home'),
    path('article/<int:pk>', article_view.as_view(), name='article'),
    path('add_post/', add_post_view.as_view(), name='add_post'),
    path('article/update/<int:pk>', update_post_view.as_view(), name='update_post'),
    path('article/<int:pk>/remove', delete_post_view.as_view(), name='delete_post'),
    path('add_category/', add_category_view.as_view(), name='add_category'),


    # this, for example, even if you dont make request from html, just by tpying in url address, will triger the related functin to run
    path('category/<str:cats>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),

]

