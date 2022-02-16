from math import pi

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rectangle(request, length, width):
    square_prem = length * width
    return render(request, 'geometry/rectangle.html')


def square(request, length: int):
    square_kvadrat = length * length
    return render(request, 'geometry/square.html')


def circle(request, radius):
    square_krug = pi * radius * radius
    return render(request, 'geometry/circle.html')


def get_rectangle_area(request, length, width):
    reverse_url = reverse('rectangle-name', args=(length, width, ))
    return HttpResponseRedirect(reverse_url)


def get_square_area(request, length):
    reverse_url = reverse('square-name', args=(length, ))
    return HttpResponseRedirect(reverse_url)


def get_circle_area(request, radius):
    reverse_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(reverse_url)
