from django.urls import path
from . import views
urlpatterns = [
    path('shows/new', views.create_show),
    path('process_show', views.process_show),
    path('shows', views.all_shows),
    path('shows/<int:id>', views.show_book),
    path('shows/<int:id>/edit', views.edit_book),
    path('shows/<int:id>/destroy', views.delete_book),
]