from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from guests_book.models import Guests


def index_view(request: WSGIRequest):
    guests = Guests.objects.filter(status='Active', is_deleted=False).order_by('-created_at')
    context = {
        'guests': guests
    }
    return render(request, 'index.html', context=context)