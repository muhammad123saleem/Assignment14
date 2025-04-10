from django.urls import path
from . import views

app_name = 'hotel'
urlpatterns = [

    path('index/',views.index_view,name='index_view'),
    path('create/',views.create_view,name='create_view'),
    path('update/<int:pk>',views.update_view,name='update_view'),
    path('delete/<int:pk>',views.delete_view,name='delete_view'),
]
