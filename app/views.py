from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),  # Здесь используем reverse
        'Показать содержимое рабочей директории': reverse('workdir')  # Здесь используем reverse
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir('.')  # Получение списка файлов в рабочей директории
    return HttpResponse('<br>'.join(files))
    # # по аналогии с `time_view`, напишите код,
    # # который возвращает список файлов в рабочей
    # # директории
    # raise NotImplemented








# from django.http import HttpResponse
# from django.shortcuts import render
# from datetime import datetime
# import os
#
# def home_view(request):
#     pages = ['/current_time/', '/workdir/']  # Список доступных страниц
#     return render(request, 'app/home.html', {'pages': pages})
#
# def current_time_view(request):
#     now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Форматирование времени
#     return HttpResponse(f'Current time: {now}')
#
# def workdir_view(request):
#     files = os.listdir('.')  # Получение списка файлов в рабочей директории
#     return HttpResponse('<br>'.join(files))
