from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
days = {'monday': 'Cписок дел, запланированных на понедельник.',
        'tuesday': 'Cписок дел, запланированных на вторник.',
        'wednesday': 'Cписок дел, запланированных на среду.',
        'thursday': 'Cписок дел, запланированных на четверг.',
        'friday': 'Cписок дел, запланированных на пятницу.',
        'saturday': 'Cписок дел, запланированных на субботу.',
        'sunday': 'Cписок дел, запланированных на воскресенье.',
        }


def get_info_about_week_day(request, week_day):
    if week_day in days.keys():
        return render(request, 'week_days/greeting.html')


def get_info_about_week_day_by_number(request, week_day: int):
    daysKeys = list(days)
    if week_day <= 7:
        reverse_urls = reverse('week_day-name', args=(daysKeys[week_day - 1], ))
        return HttpResponseRedirect(reverse_urls)
    else:
        return HttpResponse(f'Неверный номер дня: {week_day}.')
