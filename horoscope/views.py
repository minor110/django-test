from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
          "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
          "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
          "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
          "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
          "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
          "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
          "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
          "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
          "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
          "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
          "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
          }


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac.get(sign_zodiac)

    if description:
        return HttpResponseNotFound(description)
    else:
        return HttpResponseNotFound("Странный знак зодиака этот ваш " + sign_zodiac + ".")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    return HttpResponse(f'Это число {sign_zodiac}')
