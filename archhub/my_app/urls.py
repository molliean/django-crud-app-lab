# my_app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('places/', views.place_index, name='place-index'),
    path('places/<int:place_id>/', views.place_detail, name='place-detail'),
    path('places/create/', views.PlaceCreate.as_view(), name='place-create'),
    path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='place-update'),
    path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='place-delete'),
    path('places/<int:place_id>/add-hours/', views.add_hours, name='add-hours'),
    path('architects/create', views.ArchitectCreate.as_view(), name='architect-create'),
    path('architects/<int:pk>/', views.ArchitectDetail.as_view(), name='architect-detail'),
    path('architects/', views.ArchitectList.as_view(), name='architect-index'),
    path('architects/<int:pk>/update/', views.ArchitectUpdate.as_view(), name='architect-update'),
    path('architects/<int:pk>/delete/', views.ArchitectDelete.as_view(), name='architect-delete'),
    path('architects/<int:place_id>/associate-architect/<int:architect_id>/', views.associate_architect, name='associate-architect'),
    path('architects/<int:place_id>/remove-architect/<int:architect_id>/', views.remove_architect, name='remove-architect'),
    path('accounts/signup/', views.signup, name='signup'),
]
