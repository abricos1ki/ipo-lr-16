from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Магазин товаров для йоги</h1>"
        "<a href='/about/'>О магазине</a><br>"
        "<a href='/author/'>Об авторе</a>"
    )


def about(request):
    return HttpResponse(
        "Это интернет-магазин товаров для практики йоги. "
        "В продаже коврики, блоки и ремни для занятий."
    )


def author(request):
    return HttpResponse(
        "Лабораторную работу выполнил студент группы 87 TP "
        "ФИО: Саплицкий Родион"
    )

