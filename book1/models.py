from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        db_table = 'tags'
        ordering = ['title']


class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = 'category'
        ordering = ['title']


class Book(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    released = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=False)
    tag = models.ManyToManyField(Tags, blank=True)
    category = models.ManyToManyField(Category, blank=True)


    def __str__(self):
        return f"{self.title} - {self.released}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'book'
        ordering = ['released']



class Review(models.Model):
    text = models.TextField()
    book = models.ManyToManyField(
        Book
    )

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        db_table = 'reviews'
        ordering = ["text"]

