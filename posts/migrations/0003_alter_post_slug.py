# Generated by Django 4.2 on 2023-07-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
