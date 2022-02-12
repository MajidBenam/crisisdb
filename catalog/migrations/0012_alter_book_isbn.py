# Generated by Django 4.0 on 2022-01-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_bookinstance_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <span><a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a></span>', max_length=13, unique=True, verbose_name='ISBN'),
        ),
    ]