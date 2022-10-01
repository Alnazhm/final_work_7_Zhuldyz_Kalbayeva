from django.shortcuts import render, redirect, get_object_or_404
from guests_book.models import Guests
from guests_book.forms import GuestForm

def guest_edit_view(request, pk):
    guest = get_object_or_404(Guests, pk=pk)
    if request.method == "GET":
        form = GuestForm(initial={
            'author': guest.author,
            'email': guest.email,
            'description': guest.description
        })
        return render(request, 'edit_guest.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.author = form.cleaned_data['author']
            guest.email = form.cleaned_data['email']
            guest.description = form.cleaned_data['description']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'edit_guest.html', context={'form': form, 'guest': guest})
