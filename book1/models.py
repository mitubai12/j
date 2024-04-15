from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    released = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=False)

    def __str__(self):
        return f"{self.title} - {self.released}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'book'
        ordering = ['released']

