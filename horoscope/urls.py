from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_type_list),
    path('type/<stihia>', views.get_sign_type_list),
    path('<int:month>/<int:day>', views.get_month_day),
    path('task/', views.three_three_task),
    path('get-guinness-world-records/', views.get_guinness_world_records),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]