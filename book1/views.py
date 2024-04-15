from django.shortcuts import render, HttpResponse
from datetime import datetime
import random

from book1.models import Book

jokes = [
    "С отправленным на Марс американским марсоходом прервалась связь.\nЧерез неделю его нашли в Узбекистане с перебитыми номерами.",
    "Перед свадьбой думаешь, что лучше ее не бывает, перед разводом, что хужеее не бывает, и каждый раз ошибаешься!",
    "Футболист сборной России Павел Погребняк так долго сидит на скамейкезапасных 'Штутгарта', что к нему стали присматриваться грифы."
]

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It's my project")

def anekdot_view(request):
    joke = random.choice(jokes)
    if request.method == 'GET':
        return HttpResponse(joke)

def main_view(request):
    curr_datetime = datetime.now()
    time = {'curr_datetime': curr_datetime}
    return render(request, 'main.html', time)

def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books/book_list.html', context)


def book_detail_view(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return HttpResponse('Book not found', status=404)
        context = {'book': book}
        return render(request, 'books/book_detail.html', context)