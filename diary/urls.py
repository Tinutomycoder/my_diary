from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_home, name='diary_home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('entry/new/', views.create_entry, name='create_entry'),
    path('entry/<int:pk>/', views.view_entry, name='view_entry'),
    path('entry/<int:pk>/edit/', views.edit_entry, name='edit_entry'),
    path('entry/<int:pk>/delete/', views.delete_entry, name='delete_entry'),
]
