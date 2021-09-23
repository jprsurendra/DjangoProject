from django.db import models

# Create your models here.

class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)

    class Meta:
        db_table = 'tbl_books'

    def __str__(self):
        return self.title