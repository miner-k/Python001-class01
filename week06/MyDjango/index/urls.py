from django.urls import path,re_path,register_converter
from . import views,converter

register_converter(converter.IntConverter,'myint')


urlpatterns = [
    path('', views.index),
    # path('<int:year>', views.year),
    # path('<int:year>/<str:str1>',views.printstr),
    # re_path('(?P<year>^[0-9]{4}$)',views.year,name='urlyear'),
    # path('<myint:year>',views.year)
    re_path('(?P<year>[0-9]{4}).html',views.myyear,name='urlyear'),
    # path('<str:year>',views.myredicet),
]