from django.contrib import admin

# Register your models here.
from .models import Book, Author, Address, Country


# Customize admin panel
class BookAdmin(admin.ModelAdmin):
    list_filter= ("author","rating")
    list_display = ("title", "author")

# class AuthorAdmin(admin.ModelAdmin):
#     list_display=("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)