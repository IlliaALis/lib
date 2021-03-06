# Generated by Django 3.2.3 on 2021-05-31 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='author_name')),
                ('author_books', models.TextField(verbose_name='books written')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='book_name')),
                ('author_name', models.CharField(max_length=100, verbose_name='author_name')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.author')),
            ],
        ),
    ]
