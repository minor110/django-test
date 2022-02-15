from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

type_of_elements = {'fire': ['aries', 'leo', 'sagittarius'],
                    'earth': ['taurus', 'virgo', 'capricorn'],
                    'air': ['gemini', 'libra', 'aquarius'],
                    'water': ['cancer', 'scorpio', 'pisces']
                    }


def index(request):
    li_elements = ''
    for sign in list(zodiac):
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f'<ol>{li_elements}</ol>'
    return HttpResponse(response)


def get_type_list(request):
    li_elements = ''
    for sign in list(type_of_elements):
        li_elements += f"<li><a href='{sign}'>{sign.title()}</a></li>"
    response = f'<nl>{li_elements}</nl>'
    return HttpResponse(response)


def get_sign_type_list(request, stihia):
    li_elements = ''
    for element in type_of_elements.get(stihia):
        redirect_url = reverse('horoscope-name', args=[element])
        li_elements += f"<li><a href='{redirect_url}'>{element.title()}</a></li>"
    response = f"<nl>{li_elements}</nl>"
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac.get(sign_zodiac)

    if description:
        return HttpResponseNotFound(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound("Странный знак зодиака этот ваш " + sign_zodiac + ".")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Был передан неверный номер: {sign_zodiac}")

    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_urls = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_urls)
