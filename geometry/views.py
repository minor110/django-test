from math import pi

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def get_rectangle_area(request, length, width):
    square_prem = length * width
    return HttpResponse(f'Площадь прямоугольника размером {length}х{width} равна {square_prem}.')


def get_square_area(request, length):
    square_kvadrat = length * length
    return HttpResponse(f'Площадь квадрата  размером {length}х{length} равна {square_kvadrat}.')

def get_circle_area(request, radius):
    square_krug = pi * radius * radius
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {square_krug}.')