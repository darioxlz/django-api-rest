from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('items/', views.view_items, name='view_items'),
    path('items/create/', views.add_items, name='add-items'),
    path('items/<int:pk>/update/', views.update_items, name='update-items'),
    path('items/<int:pk>/delete/', views.delete_items, name='delete-items'),
]
