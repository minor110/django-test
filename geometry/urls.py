from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:length>/<int:width>/', views.rectangle, name='rectangle-name'),
    path('square/<int:length>', views.square, name='square-name'),
    path('circle/<int:radius>', views.circle, name='circle-name'),

    path('get_rectangle_area/<int:length>/<int:width>', views.get_rectangle_area),
    path('get_square_area/<int:length>', views.get_square_area),
    path('get_circle_area/<int:radius>', views.get_circle_area)
]