# Generated by Django 5.0.4 on 2024-04-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0004_rename_tag_tags_alter_tags_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='book1.category'),
        ),
    ]
