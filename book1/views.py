from django.shortcuts import render, HttpResponse
from datetime import datetime
import random

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