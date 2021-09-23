from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_notes'

    def __str__(self):
        return self.title
