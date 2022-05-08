# Generated by Django 3.2 on 2021-05-06 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.chapter', verbose_name='Текст книги'),
        ),
    ]