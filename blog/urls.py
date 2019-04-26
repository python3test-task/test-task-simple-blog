from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_pk>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('user/news/', views.news_list, name='news_list'),
    path('user/news/reading/<int:post_id>', views.add_reading, name='add_reading'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('logout/', views.logout_view, name='logout_view'),
]

