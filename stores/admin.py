from django.contrib import admin
from . models import *

admin.site.register(store)

@admin.register(books)
class booksadmin(admin.ModelAdmin):
	list_display = ['store_id','book_name','book_type','stock']