from django.contrib import admin

# Register your models here.
from .models import Book


# Customize admin panel
class BookAdmin(admin.ModelAdmin):
    list_filter= ("author","rating")
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)