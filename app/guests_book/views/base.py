from django.shortcuts import render
from guests_book.models import Guests
from guests_book.forms import GuestForm


def index_view(request):
    if request.method == "GET":
        guests = Guests.objects.filter(status='Active', is_deleted=False).order_by('-created_at')
        form = GuestForm()
        context = {
            'guests': guests,
            'form': form
        }
        return render(request, 'index.html', context=context)
