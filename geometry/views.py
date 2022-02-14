from math import pi

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rectangle(request, length, width):
    square_prem = length * width
    return HttpResponse(f'Площадь прямоугольника размером {length}х{width} равна {square_prem}.')


def square(request, length: int):
    square_kvadrat = length * length
    return HttpResponse(f'Площадь квадрата  размером {length}х{length} равна {square_kvadrat}.')


def circle(request, radius):
    square_krug = pi * radius * radius
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {square_krug}.')


def get_rectangle_area(request, length, width):
    reverse_url = reverse('rectangle-name', args=(length, width, ))
    return HttpResponseRedirect(reverse_url)


def get_square_area(request, length):
    reverse_url = reverse('square-name', args=(length, ))
    return HttpResponseRedirect(reverse_url)


def get_circle_area(request, radius):
    reverse_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(reverse_url)
