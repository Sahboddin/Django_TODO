from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='show_task'),
    path('complete_task/',views.complete_t , name= 'complete_task'),
    path('edit_task/',views.edit_t, name='edit_task'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('complete/<int:id>',views.complete, name='complete'),
]
