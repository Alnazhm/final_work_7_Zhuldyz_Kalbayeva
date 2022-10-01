from django.urls import path
from guests_book.views.base import index_view


urlpatterns = [
    path('', index_view, name='index')
    # path('guests/add/', add_view, name='guest_add'),
    # path('guests/<int:pk>/del', guest_delete_view, name='guest_deleted'),
    # path('guests/<int:pk>/edit', guest_edit_view, name='guest_edit'),
    # path('guests/<int:pk>/deleted', confirm_delete_guest_view, name='confirm_delete')
]