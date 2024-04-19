from django.contrib import admin
from book1.models import Book, Tags, Review, Category


admin.site.register(Book)
admin.site.register(Tags)
admin.site.register(Review)
admin.site.register(Category)

