
from operator import mod
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image = models.CharField(max_length=2083, default=False)
    book_available = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, max_length=200,
                                 blank=True, null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, max_length=200,
                                  blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class ImportBill(models.Model):
    note = models.CharField(max_length=255)
    staff = models.ForeignKey(User, max_length=255,
                              null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.note


class ImportBillBook(models.Model):
    importBill = models.ForeignKey(
        ImportBill, max_length=255, null=True, blank=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, max_length=255, null=True,
                             blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.importBill.id) + "-" + str(self.book.id) + "-" + str(self.quantity)


class Order(models.Model):
    product = models.ForeignKey(
        Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
