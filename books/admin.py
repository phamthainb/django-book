from django.contrib import admin
from .models import Book, Category, ImportBill, ImportBillBook, Order, Publisher

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(ImportBill)
admin.site.register(ImportBillBook)
# admin.site.register(BookTag)
# admin.site.register(BookTag)