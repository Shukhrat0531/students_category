from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('cat/<int:id>',views.category_describe,name='category_cards')

]