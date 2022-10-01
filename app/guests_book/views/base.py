from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from guests_book.models import Guests


def index_view(request: WSGIRequest):
    # guests = Guests.objects.All()
    # context = {
    #     'guests': guests
    # }
    return render(request, 'index.html')