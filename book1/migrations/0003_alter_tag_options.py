# Generated by Django 5.0.4 on 2024-04-18 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0002_tag_book_image_category_review_book_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
