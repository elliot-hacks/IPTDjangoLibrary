from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField

    def __str__(self) -> str:
        return f'{self.title}'


class Book(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    title=models.CharField(max_length=255)
    arthor=models.CharField(max_length=255)
    cover=models.ImageField(upload_to='uploads/books/')
    available=models.BooleanField(default=True)
    description=models.TextField

    def __str__(self) -> str:
        return f'{self.title} {self.arthor} {self.available}'


class BorrowedBook(models.Model):
    book=models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower=models.ForeignKey(User, on_delete=models.PROTECT)
    borrowed_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField('calculate_due_date') #Calculated based on Library policy
    returned=models.BooleanField(default=False)

    def calculate_due_date(self):
        self.due_date=self.borrowed_date + timedelta(days=14)
        self.save()

 
    def __str__(self) -> str:
        return f"{self.borrower.username}: {self.book.title}"


class bookComment(models.Model):
    borrower=models.ForeignKey(User, on_delete=models.CASCADE)
    books=models.ForeignKey(Book, on_delete=models.CASCADE)
    comment=models.TextField

    def __str__(self) -> str:
        return f"{self.borrower}"
