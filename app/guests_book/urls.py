from django.urls import path
from guests_book.views.base import index_view
from guests_book.views.guest_add_view import guest_add_view
from guests_book.views.guest_edit_view import guest_edit_view
from guests_book.views.guest_delete_view import guest_delete_view, confirm_delete_guest_view


urlpatterns = [
    path('', index_view, name='index'),
    path('guests/add/', guest_add_view, name='guest_add'),
    path('guests/<int:pk>/del', guest_delete_view, name='guest_delete'),
    path('guests/<int:pk>/edit', guest_edit_view, name='guest_edit'),
    path('guests/<int:pk>/deleted', confirm_delete_guest_view, name='confirm_delete')
]