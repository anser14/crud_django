from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('home/update/', views.update,name='update'),
    path('home/delete/<int:id>/', views.delete_data,name='delete'),
    path('home/<int:id>/', views.update_data,name='updatedata'),
]
