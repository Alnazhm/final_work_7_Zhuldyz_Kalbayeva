from django.contrib import admin
from guests_book.models import Guests


class GuestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'description', 'status', 'created_at', 'changed_at', 'is_deleted', 'deleted_at')
    list_filter = ('id', 'author', 'email', 'description', 'status', 'created_at', 'changed_at', 'is_deleted', 'deleted_at')
    search_fields = ('author', 'email', 'description', 'status',)
    fields = ('id', 'author', 'email', 'description', 'status', 'created_at', 'changed_at', 'is_deleted', 'deleted_at')

admin.site.register(Guests, GuestsAdmin)
