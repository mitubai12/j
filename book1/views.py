from django.shortcuts import render, HttpResponse, redirect
import random

from book1.models import Book
from book1.forms import BookForm, BookForm2, ReviewForm2, ReviewForm

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
    return render(request, 'main.html')

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


def book_create_view(request):
    if request.method == 'GET':
        form = BookForm2()
        return render(request, 'books/book_create.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('book_list_view')

        return render(request, 'books/book_create.html', {'form': form})


def review_create_view(request):
    if request.method == 'GET':
        form = ReviewForm2()
        return render(request, 'books/create_review.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/books')

        return render(request, 'books/book_list.html', {'form': form})