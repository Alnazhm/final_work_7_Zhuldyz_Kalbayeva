from django.shortcuts import render, redirect, get_object_or_404
from guests_book.models import Guests


def guest_delete_view(request, pk):
    guest = get_object_or_404(Guests, pk=pk)
    return render(request, 'delete_confirm_page.html', context={'guest': guest})

def confirm_delete_guest_view(request, pk):
    guest = get_object_or_404(Guests, pk=pk)
    guest.delete()
    return redirect('index')