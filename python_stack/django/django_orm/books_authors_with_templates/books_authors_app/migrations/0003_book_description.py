# Generated by Django 2.2.4 on 2022-09-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_publisher_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='add discription'),
            preserve_default=False,
        ),
    ]
