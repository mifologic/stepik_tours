from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    if not departure:
        return HttpResponseNotFound(f"Нет направления {departure}")
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    if not tour_id:
        return HttpResponseNotFound(f"Нет направления {tour_id}")
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена. Зайдите попозже.')


def custom_handler500(request, exception):
    return HttpResponseServerError('Сервер недоступен. Зайдите попозже.')
