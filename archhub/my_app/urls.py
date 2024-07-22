from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('places/', views.place_index, name='place-index'),
    path('places/<int:place_id>/', views.place_detail, name='place-detail'),
    path('places/create/', views.PlaceCreate.as_view(), name='place-create'),
    path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='place-update'),
    path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='place-delete'),
]
