from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:category_id>/', views.category, name='category'),
    path('create_post/', views.create_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('logout/', views.logout_view, name='logout_view'),
    path('create_category/', views.create_category, name='create_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
]
