from django.shortcuts import render, redirect
from guests_book.models import Guests
from guests_book.forms import GuestForm

def guest_add_view(request):
    form = GuestForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'add_guest.html', context)
    form = GuestForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'add_guest.html', context)
    guest = Guests.objects.create(**form.cleaned_data)
    return redirect('index')