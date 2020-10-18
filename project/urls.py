from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.add_show, name='add_show'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update'),
]